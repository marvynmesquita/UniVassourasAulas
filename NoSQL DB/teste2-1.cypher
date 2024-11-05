WITH [
    {Brasil:["Verde", "Amarelo", "Azul"]},
    {Argentina:["Azul", "Branco"]},
    {Chile: ["Vermelho", "Branco", "Azul"]},
    {Paraguai: ["Vermelho", "Branco", "Azul"]},
    {Uruguai: ["Azul", "Branco"]},
    {Inglaterra: ["Vermelho", "Branco"]},
    {França: ["Azul", "Branco", "Vermelho"]},
    {Espanha: ["Vermelho", "Amarelo"]},
    {`Estados Unidos`: ["Vermelho", "Branco", "Azul"]},
    {Alemanha: ["Preto", "Vermelho", "Amarelo"]},
    {Itália: ["Verde", "Branco", "Vermelho"]},
    {Rússia: ["Branco", "Azul", "Vermelho"]},
    {Japão: ["Branco", "Vermelho"]},
    {Canadá: ["Vermelho", "Branco"]}
] as paises

UNWIND paises as pais

WITH pais
UNWIND range(0, size(pais[coalesce(keys(pais))[0]])-1) AS index
    MERGE(p:Pais{Nome: coalesce(keys(pais))[0]})
    SET p.Nome = coalesce(keys(pais))[0]
    SET p.Cores = coalesce(p.Cores, []) +  pais[coalesce(keys(pais))[0]][index]
    

WITH [
    {`Guerra do Paraguai`:[{Brasil: ["Atacante", "Vitoria"]}, {Argentina: ["Atacante", "Vitoria"]}, {Paraguai: ["Defensor", "Derrota"]}]},
    {`Guerra da Independência do Brasil`:[{Brasil: ["Atacante", "Vitoria"]}]},
    {`Guerra das Malvinas`: [{Inglaterra: ["Defensor", "Vitoria"]}, {Argentina: ["Atacante", "Derrota"]}]},
    {`Guerra da Secessão`: [{`Estados Unidos`: ["Defensor", "Vitoria"]}]},
    {`Guerra do Vietnã`: [{`Estados Unidos`: ["Atacante", "Derrota"]}]},
    {`Guerra Franco-Prussiana`: [{França: ["Defensor", "Derrota"]},{Prússia: ["Atacante", "Vitoria"]}]},
    {`Guerra Russo-Japonesa`: [{Japão: ["Atacante", "Vitoria"]}, {Rússia: ["Defensor", "Derrota"]}]},
    {`Primeira Guerra Mundial`: [{Alemanha: ["Atacante", "Derrota"]}, {França: ["Defensor", "Vitoria"]}]},
    {`Segunda Guerra Mundial`: [{Alemanha: ["Atacante", "Derrota"]}, {`Estados Unidos`: ["Atacante", "Vitoria"]}]}
] as guerras

UNWIND guerras as guerra

WITH guerra
UNWIND range(0, size(guerra[coalesce(keys(guerra))[0]])-1) AS index
    MERGE(g:Guerra{Nome: coalesce(keys(guerra))[0]})

WITH 1 AS nada

MATCH(p:Pais) WHERE "Branco" in p.Cores RETURN p