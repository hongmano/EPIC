library(data.table)
library(dplyr)

dat <- fread('https://raw.githubusercontent.com/hongmano/EPIC/main/fin.csv')

assy <- dat %>% 
  filter(x > 0 & y > 0) %>% 
  select(x, y) %>% 
  unique %>% 
  arrange(y)

assy <- split(assy, assy$y)
for(i in 1:length(assy)){
  
  if (i %% 2 == 1) {
    
    assy[[i]] <- assy[[i]] %>% 
      arrange(x)
    
  }else {
    
    assy[[i]] <- assy[[i]] %>% 
      arrange(desc(x))
    
  }
  
}
assy <- rbindlist(assy) %>% 
  mutate(assy = 1:1334)

dat <- dat %>% 
  filter(HB %in% c(2,6)) %>% 
  mutate(fail = ifelse(HB == 6 & (NB != 0 | V192 != 0), 1, 0)) %>% 
  select(run, wf, x, y, fail)

dat <- dat %>% 
  inner_join(assy)

fin <- dat 
# -------------------------------------------------------------------------

assy_simulation <- function(fin){

  run_wf_list <- fin %>% 
    select(run, wf) %>% 
    unique
  
  run_wf_list <- run_wf_list %>% 
    mutate(wf_order = sample(1:nrow(run_wf_list)))
  
  fin <- fin %>% 
    inner_join(run_wf_list, by = c('run', 'wf')) %>% 
    arrange(wf_order, run, wf, assy)

  assy_done <- list()
  
  # -------------------------------------------------------------------------
  
  main_wf <- fin %>% 
    filter(wf_order == 1)
  
  add_wf <- fin %>% 
    filter(wf_order == 2)
  
  n_pkg <- floor(min(nrow(main_wf) / 2, nrow(add_wf) / 2))
  
  main_etc <- nrow(main_wf) - n_pkg * 2
  add_etc <- nrow(add_wf) - n_pkg * 2
  
  main_wf$pkg <- c(rep(paste(1, 1:n_pkg, sep = '_'), each = 2), rep('etc', main_etc)) 
  add_wf$pkg <- c(rep(paste(1, 1:n_pkg, sep = '_'), each = 2), rep('etc', add_etc)) 
  
  assy_done[[1]] <- rbind(
    
    main_wf %>% filter(pkg != 'etc'),
    add_wf %>% filter(pkg != 'etc')
    
  ) %>% 
    arrange(pkg)
  
  main_wf <- rbind(
    
    add_wf %>% 
      filter(pkg == 'etc'),
    main_wf %>% 
      filter(pkg == 'etc')
    
  ) %>% 
    arrange(wf_order, assy)
  
  if (length(table(main_wf$wf_order)) > 1 & nrow(main_wf) > 4) {
    
    main_wf$pkg <- c(rep(paste(1, 'etc_1', sep = '_'), 4), rep('etc', nrow(main_wf) - 4))
    
    assy_done[[1]] <- assy_done[[1]] %>% 
      rbind(main_wf %>% 
              filter(pkg != 'etc'))
    
    main_wf <- main_wf %>% 
      filter(pkg == 'etc')
    
  }
  
  # -------------------------------------------------------------------------
  
  for(i in 3:nrow(run_wf_list)) {
    
    add_wf <- fin %>% 
      filter(wf_order == i)
    
    n_pkg <- floor(min(nrow(main_wf) / 2, nrow(add_wf) / 2))
    
    if (n_pkg == 0 & i != nrow(run_wf_list)) {
      
      main_wf <- rbind(main_wf %>% 
                         select(-pkg), add_wf)
      next
      
    }
    
    main_etc <- nrow(main_wf) - n_pkg * 2
    add_etc <- nrow(add_wf) - n_pkg * 2
    
    main_wf$pkg <- c(rep(paste(i - 1, 1:n_pkg, sep = '_'), each = 2), rep('etc', main_etc)) 
    add_wf$pkg <- c(rep(paste(i - 1, 1:n_pkg, sep = '_'), each = 2), rep('etc', add_etc)) 
    
    assy_done[[i - 1]] <- rbind(
      
      main_wf %>% filter(pkg != 'etc'),
      add_wf %>% filter(pkg != 'etc')
      
    ) %>% 
      arrange(pkg)
    
    main_wf <- rbind(
      
      add_wf %>% 
        filter(pkg == 'etc'),
      main_wf %>% 
        filter(pkg == 'etc')
      
    ) %>% 
      arrange(wf_order, assy)
    
    if (length(table(main_wf$wf_order)) > 1 & nrow(main_wf) > 4) {
      
      main_wf$pkg <- c(rep(paste(i - 1, 'etc_1', sep = '_'), 4), rep('etc', nrow(main_wf) - 4))
      
      assy_done[[i - 1]] <- assy_done[[i - 1]] %>% 
        rbind(main_wf %>% 
                filter(pkg != 'etc'))
      
      main_wf <- main_wf %>% 
        filter(pkg == 'etc')
      
    }
  }
  
  if (nrow(main_wf) > 3) {
    
    final_etc <- nrow(main_wf) %% 4
    main_wf <- head(main_wf, nrow(main_wf) - final_etc)
    
    final_pkg <- nrow(main_wf) / 4
    
    if (final_pkg > 0) {
      
      assy_done[[i]] <- main_wf %>% 
        mutate(pkg = rep(paste(i, 1:final_pkg, sep = '_'), each = 4))
      
    }
    
  }
  
  assy_done <- rbindlist(assy_done)
  
  print(fin %>% 
          filter(wf_order == nrow(run_wf_list)) %>% 
          select(run, wf) %>% 
          write.csv())
  
  return(assy_done)
  
}

result <- list()

for (trial in 1:30) {

  set.seed(trial)
  result[[trial]] <- assy_simulation(dat)

}

result[[1]] %>% 
  group_by(pkg) %>% 
  summarise(fail = max(fail)) %>% 
  select(fail) %>% 
  unlist %>% 
  mean

dat$pkg <- rep(1:18311, each = 4)

dat %>% 
  group_by(pkg) %>% 
  summarise(fail = max(fail)) %>% 
  select(fail) %>% 
  unlist %>% 
  mean
library(ggplot2)
dat %>% 
  group_by(run, x, y) %>% 
  summarise(fail = mean(fail)) %>% 
  ggplot(aes(x = x,y = y, fill = fail))+
  geom_tile() +
  scale_fill_gradient(low = 'blue', high = 'red') +
  facet_wrap(~ run) +
  theme_bw() +
  theme(legend.position = 'none')
