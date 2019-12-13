*** Settings ***
Library             SeleniumLibrary
Library             LoginPage.py

*** Keywords ***
Generic Suite Setup
    [Arguments]    ${browser}=${global_browser}    ${timeout}=${global_timeout}    ${logLevel}=INFO    ${base_url}=${global_base_url}
    Set Log Level    ${logLevel}
    Open Browser    browser=${browser}    url=${base_url}
    Maximize Browser Window
    Set Selenium Timeout    ${timeout}
    Register Keyword To Run On Failure    ${EMPTY}

Input username
    [Arguments]  ${username}
        Input Text  name=uname  ${username}
Input pwd
    [Arguments]  ${password}
        Input Text    name=psw    ${password}
click login button
    Click Button  name=submit

Open Login Page
    Go To    ${global_base_url}

Generic Suite Teardown
    Delete All Cookies
    Close All Browsers    