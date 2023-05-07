
library(rvest)

lines = readLines(file("wikipedia_knowledge"))


gets = grepl("XXXdiseaseXXX", lines)
tops = lines[gets]
gets = c(FALSE, gets)
gets = gets[-length(gets)]
articles = lines[gets]

lines_result = character()

urls = paste0("https://en.wikipedia.org/wiki/", articles)
urls = stringr::str_replace_all(urls, " ", "_")


get_page = function(url){
  html = read_html(url)
  g = html %>% html_nodes("p") %>% html_text2()
  g = g[nchar(g) > 2]
  # Get rid of citations
  g = stringr::str_replace_all(g, "\\[[^\\]]*\\]", "")
  g_try = stringr::str_replace_all(g, "\\.:.[^\\s*]+", ".")
  return(g_try)
}

for(i in 1:length(urls)){
  lines_result = c(lines_result, tops[i], articles[i], "")
  result = get_page(urls[i])
  lines_result = c(lines_result, result, "", "", "XXXendXXX")
}


file_connect = file("wikipedia_knowledge_new")
writeLines(lines_result, file_connect)
close(file_connect)