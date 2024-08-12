const tamanho = 10;

function createTriangleRect (tamanho) {
    for( a = 1; a < tamanho + 1; a++) {
        let line = ''
        for(b = 0; b < a; b++) {
            line += '*';
        }
        console.log(line);
    }
}

createTriangleRect(tamanho);