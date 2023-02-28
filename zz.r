
# 1. Options / Packages ---------------------------------------------------

library(bigdataquery)
library(dplyr)
library(ggplot2)
library(plotly)
library(data.table)
library(reshape2)
library(stringr)
library(readxl)
library(grid)
library(gridExtra)
library(showtext)
library(lubridate)
library(formattable)
library(htmltools)
library(webshot)
library(htmltools)
library(rmarkdown)
install.packages('rmarkdown')
today <- Sys.time()

# 2. Data Loading ---------------------------------------------------------

sql <- '

  select 
  
  lot_id, step_id, end_time, part_id, program_name, test_count, pass_count, tester_name, tester_number, retest_count, 
  category_01, category_02,
  revno, final_ng_cnt, site, simax_ncp_code
  
  
  from (
  
    select substr(part_id, 1, 10) as pk, *
    from pkg.t_srt_finaltest_lot
    where 
    (
    substr(step_id, 1, 4) = "T070" or 
    substr(step_id, 1, 4) = "T071" or 
    substr(step_id, 1, 4) = "T072" or 
    substr(step_id, 1, 4) = "T090" or 
    substr(step_id, 1, 4) = "T091"
    ) and
    
    end_time between "before" and "after"
  
  ) as b
  
  where 
  
  (
  pk = "K3KL3L30CM" or 
  pk = "K3KL5L50CM" or 
  pk = "K3KL8L80CM" or 
  pk = "K3KL9L90CM" or 
  pk = "K3KLALA0CM" or 
  pk = "K3LK7K70CM" or 
  pk = "K3KLBLB0CM" or 
  
  pk = "K3LKEKE0CM" or
  pk = "K3LKWKW0CM" or 
  pk = "K3LKOKO0CM"
  )

  
'

sql <- sql %>% 
  str_replace_all('before', as.character(today - 24 * 60 * 60 * 24)) %>% 
  str_replace_all('after', as.character(today + 1 * 60 * 60 * 24))

oscar <- getData(sql = sql)

oscar <- oscar %>% 
  group_by(lot_id, step_id, program_name, revno) %>% 
  summarise(end_time = max(end_time)) %>% 
  inner_join(oscar) %>% 
  mutate(yld = pass_count / test_count) %>% 
  unique

hft <- oscar %>% 
  filter(step_id %in% c('T072129', 'T090129', 'T090128', 'T091128', 'T090064', 'T091064')) %>% 
  mutate(PKG = substr(part_id, 1, 12),
         MASK = substr(part_id, 22, 22),
         week = paste0('W', week(end_time)))

# 3. YLD ------------------------------------------------------------------

yld <- hft %>% 
  mutate(yld = ifelse(substr(step_id, 5, 7) == '129', category_01 / test_count, category_02 / test_count),
         yld = yld * 100)

ggplotly(
  
  yld %>% 
    arrange(week, MASK) %>% 
    filter(substr(step_id, 5, 7) == '128') %>% 
    filter(yld > 75) %>% 
    ggplot(aes(x = week,
               y = yld,
               col = MASK)) +
    geom_jitter() +
    facet_wrap(~ paste(step_id, PKG, sep = '_'), nrow = 2) +
    theme_bw()
  
)




# 3. NGBIN ----------------------------------------------------------------

ngbin <- hft$final_ng_cnt
ngbin_list <- c()

for (i in 1:length(ngbin)) {
  
  ngbin_list[[i]] <- ngbin[i] %>% 
    str_split(',') %>% 
    unlist %>% 
    str_split(':') %>% 
    unlist %>% 
    matrix(ncol = 2, byrow = T) %>% 
    as.data.frame() %>% 
    `colnames<-`(c('TN', 'n')) %>% 
    mutate(TN = as.numeric(TN),
           n = as.numeric(n)) %>% 
    na.omit() %>% 
    filter(TN < 5000) %>% 
    cbind(hft[i, ] %>% 
            select(-final_ng_cnt))
  
}

ngbin_list <- rbindlist(ngbin_list)
ngbin_list <- ngbin_list %>% 
  group_by(PKG, step_id, week, TN) %>% 
  summarise(n = sum(n)) %>% 
  inner_join(hft %>% 
               group_by(PKG, week, step_id) %>% 
               summarise(all = sum(test_count))) %>% 
  mutate(PORTION = n / all)


# 4. TGR ------------------------------------------------------------------

total_gross <- oscar %>% 
  mutate(STEP = substr(step_id, 1, 4),
         week = paste0('W', week(end_time))) %>% 
  group_by(STEP, week) %>% 
  summarise(test_count = sum(test_count),
            pass_count = sum(pass_count)) %>% 
  mutate(YLD = pass_count / test_count) %>% 
  dcast(week ~ STEP, value.var = 'YLD') %>% 
  mutate(T072 = ifelse(is.na(T072) == T, 1, T072),
         TGR = T070 * T071 * T072 * T090 * T091) %>% 
  mutate_if(is.numeric,
            function(x) percent(x)) %>% 
  inner_join(oscar %>% 
               mutate(week = paste0('W', week(end_time))) %>% 
               group_by(week) %>% 
               summarise(TEST_SUM = sum(test_count)))

test <- formattable(total_gross,
                    list(table.attr = 'style="border: 3px solid black;";\"'))


export_formattable <- function(f, file, width = "100%", height = NULL, 
                               background = "white", delay = 0.2)
{
  w <- as.htmlwidget(f, width = width, height = height)
  path <- html_print(w, background = background, viewer = NULL)
  url <- paste0("file:///", gsub("\\\\", "/", normalizePath(path)))
  webshot(url,
          file = file,
          selector = ".formattable_widget",
          delay = delay)
}

setwd('C:/Users/mano.hong/Desktop')
export_formattable(test, 'test.png')
