*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  antti
    Set Password  antti123
    Set Password Confirmation  antti123
    Click Register
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  aa
    Set Password  antti123
    Set Password Confirmation  antti123
    Click Register
    Element Should Be Visible  tag:li
    Element Should Contain  tag:li  Username is too short, minimun length is 3
    
Register With Valid Username And Too Short Password
    Set Username  toimitusjohtaja
    Set Password  aa111
    Set Password Confirmation  aa111
    Click Register
    Element Should Be Visible  tag:li
    Element Should Contain  tag:li  Password is too short, minimum length is 8

Register With Nonmatching Password And Password Confirmation
    Set Username  toimitusjohtaja
    Set Password  aabbccdd1
    Set Password Confirmation  aabbccdd2
    Click Register
    Element Should Be Visible  tag:li
    Element Should Contain  tag:li  Password confirmation does not match

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Click Register
    Click Button  Register
