*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input New Command  new
    Input Credentials  keijo  keijo123
    Output Should Contain  New user registered

#Register With Already Taken Username And Valid Password
    Input New Command  new
    Input Credentials  keijo  keijo123
    Output Should Contain  New user registered
    Input New Command  new
    Input Credentials  keijo  toimitusjohtaja11111
    Output Should Contain  Username is taken

Register With Too Short Username And Valid Password
    Input New Command  new
    Input Credentials  aa  keijo123
    Output Should Contain  Username is too short, minimum length is 3

Register With Valid Username And Too Short Password
    Input New Command  new
    Input Credentials  toimitusjohtaja  kissa12
    Output Should Contain  Password is too short, requirements are minimun length of 8 followed with one number

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command  new
    Input Credentials  keijo  aabbccdd
    Output Should Contain  Password is too short, requirements are minimun length of 8 followed with one number