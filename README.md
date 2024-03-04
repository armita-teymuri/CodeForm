# CodeForm
Code formatter/beautifier for **Kotlin** programming language

## Components
```mermaid
flowchart LR

CF[CodeForm] --> B(Cleaner)
CF[CodeForm] --> B(Formatter)
```


## Kotlin Testcases
|Testcase  |V 0.1.0     |
|----------|------------|
|Test1     |![](_/c.png)|
|Test2     |![](_/c.png)|
|Test3     |![](_/u.png)|
|Test4     |![](_/u.png)|
|Test5     |![](_/u.png)|
|Test6     |![](_/u.png)|
|Test7     |![](_/u.png)|


## Extensions
### Status
|Version   |VSCode      |
|----------|------------|
|0.1.0     |![](_/u.png)|

### Setup extension
- To setup extension project `yo code`

### Run extension
- In vscode open `extension.js` and push <kbd>F5</kbd> and select `VS Code Extension Developement`
- In new vscode window, hit <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> and search select `Open Code Formatter Kotlin`

### Test extension
- Install [Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
- From left side of IDE, Under Extensions, Click on `testing` button

## Future Work
- ![](_/u.png) Setup vscode extension
- ![](_/u.png) Deploy in marketplace
- ![](_/u.png) Format code indentation
- ![](_/u.png) Custom commands to customize formatter
- ![](_/u.png) Setup unit tests in `tests` directory

## Rules for commits
1. New Testcase: `Setup testcase no [NUMBER], [DESCIPTION]`, last one was 8
1. Update Testcase: `Update testcase no [NUMBER], [DESCIPTION]`
1. Update for Formatted Testcases: `Update formatted testcases [TRY_NUMBER]`
