mkdir -p ~/.streamlit/


echo "\
[general]\n\
email=\"youremail@domain.com\"\n\
" >~/.streamlit/credentials.toml
[server]\n\
headless = true\n\
enableCORS = false\n\
port= $port\n\
" >~/.streamlit/config.toml
