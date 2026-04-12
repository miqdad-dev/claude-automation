const board = document.getElementById('game-board');
const boxes = [];
const empty = { x: 200, y: 200 };

for (let i = 0; i < 8; i++) {
    const div = document.createElement('div');
    div.style.left = `${(i % 3) * 100}px`;
    div.style.top = `${Math.floor(i / 3) * 100}px`;
    div.className = 'box';
    div.textContent = i + 1;
    div.addEventListener('click', () => {
        const dx = Math.abs(empty.x / 100 - div.offsetLeft / 100);
        const dy = Math.abs(empty.y / 100 - div.offsetTop / 100);
        if ((dx + dy) > 1) return;
        const { style } = div;
        [style.left, style.top] = [empty.x + 'px', empty.y + 'px'];
        [empty.x, empty.y] = [div.offsetLeft, div.offsetTop];
    });
    boxes.push(div);
    board.appendChild(div);
}