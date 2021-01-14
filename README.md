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

## Especializar models
As models ser especializar as models por exemplo o todo ter uma model task outra labels e etc

##Adapters funcionarem como lib
Usar sub modules do git nos adapters

## ORM
Selects tem que ser sempre otimizados

## Linter
Rodar o prospector

    return Gino(
        dsn=settings.DB_DSN,
        pool_min_size=settings.DB_POOL_MIN_SIZE,
        pool_max_size=settings.DB_POOL_MAX_SIZE,
        echo=settings.DB_ECHO,
        ssl=settings.DB_SSL,
        use_connection_for_request=settings.DB_USE_CONNECTION_FOR_REQUEST,
        retry_limit=settings.DB_RETRY_LIMIT,
        retry_interval=settings.DB_RETRY_INTERVAL,
    )

Try Catch nos endpoints
