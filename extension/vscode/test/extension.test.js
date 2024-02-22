const assert = require('assert');
const vscode = require('vscode');
const extension = require('../extension');

// Install https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner
// From left side of IDE; Under Extensions; Click on `testing` button

suite('Extension Test Suite', () => {
	vscode.window.showInformationMessage('Start all tests.');

	test('Sample test', () => {
		assert.strictEqual(-1, [1, 2, 3].indexOf(5));
		assert.strictEqual(-1, [1, 2, 3].indexOf(0));
	});
});
