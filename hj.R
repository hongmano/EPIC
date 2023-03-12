
# 1. Options / Packages ---------------------------------------------------

# library(bigdataquery)
library(dplyr)
library(ggplot2)
library(plotly)
library(data.table)
library(reshape2)
library(stringr)
library(grid)
library(gridExtra)
library(showtext)
library(lubridate)
library(formattable)
library(htmltools)
library(webshot)
library(htmltools)


today <- Sys.time()

setwd('C:/Users/mshj9/Desktop/mano')

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
  
  substr(pk, 1, 2) = "K3" and substr(pk, 9, 2) = "CM"

  
'

sql <- sql %>% 
  str_replace_all('before', as.character(today - 24 * 60 * 60 * 24)) %>% 
  str_replace_all('after', as.character(today + 1 * 60 * 60 * 24))

oscar <- getData(sql = sql)

hft <- oscar %>% 
  group_by(lot_id, step_id, program_name, revno) %>% 
  summarise(end_time = max(end_time)) %>% 
  inner_join(oscar) %>%  
  unique %>% 
  filter(step_id %in% c('T072129', 'T090129', 'T090128', 'T091128', 'T090064', 'T091064')) %>% 
  mutate(PKG = substr(part_id, 1, 12),
         MASK = paste0('15.0', substr(part_id, 22, 22)),
         week = paste0('W', week(end_time)))

# 3. YLD ------------------------------------------------------------------

hft <- fread('dat.csv')
def <- fread('496_MOB.csv')

yld <- hft %>% 
  group_by(PKG, MASK, step_id, week) %>% 
  summarise(category_01 = sum(category_01),
            category_02 = sum(category_02),
            input = sum(test_count)) %>% 
  mutate(YLD = ifelse(step_id %in% c('T072129', 'T090129'), category_01 / input, category_02 / input)) %>% 
  select(-c(category_01, category_02)) %>% 
  ungroup() %>% 
  mutate(input = paste0('(', round(input / 1000, 1), 'K)'),
         YLD = paste(percent(YLD), input)) %>% 
  dcast(step_id + PKG + MASK ~ week) %>% 
  mutate_at(vars(starts_with('W')), .funs = function(x) ifelse(is.na(x) == T, '-', x)) %>% 
  mutate(step_id = ifelse(step_id == 'T072129', 'HFH(8.5Gbps)',
                          ifelse(step_id == 'T090129', 'HFC(8.5Gbps)',
                                 ifelse(substr(step_id, 1, 4) == 'T090', 'HFC', 'HFH')))) %>% 
  mutate(step_id = factor(step_id, levels = c('HFH(8.5Gbps)', 'HFC(8.5Gbps)', 'HFC', 'HFH'))) %>% 
  arrange(PKG, MASK, step_id)

yld <- formattable(yld,
                   list(table.attr = 'style="border: 3px solid black;";\"'))


# 3. NGBIN ----------------------------------------------------------------

ngbin <- hft$final_ng_cnt
ngbin_list <- c()

for (i in 1:length(ngbin)) {
  
  ngbin_list[[i]] <- ngbin[i] %>% 
    str_split(',|:') %>% 
    unlist %>% 
    matrix(ncol = 2, byrow = T) %>% 
    as.data.frame() %>% 
    `colnames<-`(c('TN', 'n')) %>% 
    mutate(TN = as.numeric(TN),
           n = as.numeric(n)) %>% 
    na.omit() %>% 
    filter(TN < 5000 & TN != 4996 & TN != 4405)
  
  if (nrow(ngbin_list[[i]]) > 0) {
    
    ngbin_list[[i]] <- ngbin_list[[i]] %>% 
      cbind(hft[i, ] %>% 
              select(-final_ng_cnt))
    
  } else {
    
    ngbin_list[[i]] <- hft[i, ]
    
  }
  
}

ngbin_list <- rbindlist(ngbin_list, fill = T) %>% 
  group_by(PKG, MASK, step_id, week, TN) %>% 
  summarise(n = sum(n)) %>% 
  inner_join(hft %>% 
               group_by(PKG, MASK, step_id, week) %>% 
               summarise(all = sum(test_count))) %>% 
  mutate(PORTION = n / all,
         STEP = ifelse(substr(step_id, 1, 4) %in% c('T072', 'T091'), 'HFH', 'HFC')) %>% 
  left_join(def) %>% 
  left_join(yld) %>% 
  mutate(PORTION = PORTION * 1000000,
         yld_7.5 = percent(yld_7.5),
         yld_8.5 = percent(yld_8.5)) %>% 
  ungroup()

plot_info <- dat %>% 
  select(week, MASK, input, yld_7.5, yld_8.5) %>% 
  unique %>% 
  arrange(week, MASK) %>% 
  t()

plot_info <- cbind(matrix(nrow = 5, ncol = 4, data = ''), rownames(plot_info), plot_info) %>% 
  as.data.frame()

item <- dat %>% 
  select(category, tCK, VDD, TN, PATN, MASK, week, PORTION) %>% 
  dcast(category + tCK + VDD + TN + PATN ~ week + MASK) %>% 
  mutate_at(vars(starts_with('W')), .funs = function(x) {x <- ifelse(is.na(x) == T, 0, round(x, 0))}) %>% 
  `colnames<-`(names(plot_info))

item <- item %>% 
  mutate(rank = rowSums(item[, 6:ncol(item)])) %>% 
  arrange(desc(rank)) %>% 
  select(-rank)

plot_fin <- rbind(plot_info, item) %>% 
  as.data.frame()

plot_fin <- formattable(plot_fin,
                        list(table.attr = 'style="border: 3px solid black;";\"'))


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
