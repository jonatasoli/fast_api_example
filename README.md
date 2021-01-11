# Excessões

## Estrutura de pastas
Se model, schema, adapter, services e dao forem poucos modelos tipo uns 8 não precisaria manter a estrutura de pastas

## SqlAlchemy
Podemos usar o Gino que faz uma abstração async da engine do sqlalchemy mantendo o resto do orm como o original
Podemos usar o SQLAlchemy 1.4beta que já tem um alpha da estrutura async

## Quando poderiamos usar algo como um ViewModel?
Quando o objeto que vem para o Endpoint só já vem pra ser armazenado no banco e não precisa fazer mais NADA, poderiamos deixar fazer uma das opções abaixo:
1 - Salvar o objeto diretamente no endpoints (o próprio objeto db pode ser adicionado no método)
2 - Passar o modelo diretamente pra DAO 
