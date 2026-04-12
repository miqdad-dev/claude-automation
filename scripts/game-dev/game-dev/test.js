const assert = require('assert');

function runTests() {
    assert.equal(document.getElementsByClassName('box').length, 8);
    assert.equal(document.getElementById('game-board').children.length, 8);
    for (let i = 0; i < 8; i++) {
        const box = document.getElementsByClassName('box')[i];
        assert.equal(box.textContent, i + 1);
        assert.equal(box.offsetLeft, (i % 3) * 100);
        assert.equal(box.offsetTop, Math.floor(i / 3) * 100);
    }
}

runTests();