document.addEventListener('DOMContentLoaded', () => {
    const table = document.getElementById('example2');
    const headers = table.querySelectorAll('th');

    headers.forEach(header => {
        // Create a resize handle and append it to each header
        const resizeHandle = document.createElement('div');
        resizeHandle.className = 'resize-handle';
        header.appendChild(resizeHandle);

        resizeHandle.addEventListener('mousedown', (e) => {
            e.preventDefault();
            const startX = e.clientX;
            const startWidth = header.offsetWidth;

            const onMouseMove = (moveEvent) => {
                const newWidth = startWidth + (moveEvent.clientX - startX);
                header.style.width = `${newWidth}px`;
                // Update column widths for other rows
                table.querySelectorAll('tbody tr').forEach(row => {
                    row.children[header.cellIndex].style.width = `${newWidth}px`;
                });
            };

            const onMouseUp = () => {
                document.removeEventListener('mousemove', onMouseMove);
                document.removeEventListener('mouseup', onMouseUp);
            };

            document.addEventListener('mousemove', onMouseMove);
            document.addEventListener('mouseup', onMouseUp);
        });
    });
});
