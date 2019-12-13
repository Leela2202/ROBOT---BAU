*** Settings ***
Documentation       Example using the space separated plain text format.
Library             OperatingSystem
Library             resource/LoginPage.py
Library             SeleniumLibrary
Library             DataDriver  sample_testdata1.csv
Test Template       Invalid login
Suite Setup         Generic Suite Setup
Suite Teardown      Generic Suite Teardown
Test Teardown       Generic Test Teardown
Test Setup          Open Login Page
Resource            resource/common.robot

*** Variables ***
${MESSAGE}       Hello, world!
${username}
${password}
${global_timeout}       5s
${global_browser}       
${global_base_url}      file:///C:/Users/Deepak/Desktop/hello.html

*** Test Case ***
Login with user ${username} and password ${password}

*** Keywords ***
Invalid login
    [Arguments]  ${username}  ${password}
    Input username  ${username}
    Input pwd  ${password}
    click login button
    Error page should be visible
