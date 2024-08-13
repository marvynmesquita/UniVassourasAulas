let obj = {
    nome: 'Marvyn',
    idade: 32,
    getObj: function()  {
        return this;
    }
};

console.log(obj.getObj());