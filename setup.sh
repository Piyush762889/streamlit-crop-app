mkdir -p ~/.streamlit/


echo "\
[general]\n\
email=\"piyush030891@gmail.com\"\n\
" >~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
port= $port\n\
" >~/.streamlit/config.toml
