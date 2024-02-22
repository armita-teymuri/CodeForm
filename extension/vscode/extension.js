const vscode = require('vscode');

function activate(context) {
	console.log('"open-formatter" is activated');

	let disposable = vscode.commands.registerCommand('open-formatter.kotlin', function () {
		vscode.window.showInformationMessage('Open Formatter is Called');
	});

	context.subscriptions.push(disposable);
}

function deactivate() {
	console.log('"open-formatter" is deactivated');
}

module.exports = {
	activate,
	deactivate
}
