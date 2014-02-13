## Fabfile for Dreamhost

Projeto do Fabric que realiza o bootstrap de um ambiente no Dreamhost (http://www.dreamhost.com) contendo:

- Python 2.7.6
- SetupTools 0.6c11
- Pip 1.5.2
- MySQL-python 1.2.3
- Python Imaging Library (PIL) 1.1.7
- Virtualenv 1.11.2

### Requisitos:

- Conta no host Dreamhost (http://www.dreamhost.com);
- Fabric instalado (http://fabfile.org).

### Passos:

#### 1) Setar as seguintes variáveis de ambiente antes de executar o script:

  - DH_USER: O nome do usuário no Dreamhost;
  - DH_PASSWORD: A senha que seu usuário usa para acessar via SSH;
  - DH_HOST: O endereço do servidor do seu usuário/site.

Exemplo:

```
export DH_USER=fernandoe
export DH_PASSWORD=Senha
export DH_HOST=espindola.info 
```

#### 2) Comando para executar o script:

```
fab dh boostrap
```

Pronto, agora é entrar no servidor e começar a instalar libs e configurar o seu projeto.

### Pessoal, ajudem a manter e melhorar o script.

* Observação: Testado com Fabric 1.8.1

