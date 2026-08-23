# Instalação das ferramentas

Este tutorial instala o **IEDA**, o **MOPAC** e o **VMD 2** em um ambiente
Linux. O IEDA e o MOPAC ficam no mesmo ambiente Conda, enquanto o VMD 2 é
instalado na pasta pessoal do usuário, sem necessidade de `sudo`.

## Pré-requisitos

É necessário ter o Git e o Conda instalados. O Conda pode ser obtido pelo
[Miniconda](https://docs.conda.io/projects/miniconda/en/latest/).

Os comandos abaixo devem ser executados em um terminal Bash.

## IEDA e MOPAC

Clone o repositório do IEDA e entre na pasta do projeto:

```bash
git clone https://github.com/anchieta-oliveira/IEDA.git
cd IEDA/
```

Crie o ambiente Conda do curso e ative-o:

```bash
conda create -n IEDA python=3.12
conda activate IEDA
```
Instale o IEDA a partir do próprio repositório:

```bash
pip install .
```

y
Instale o MOPAC pelo Conda:

```bash
conda install -c conda-forge mopac
```


Teste as duas ferramentas:

```bash
mopac
IEDA --help
```

O comando `mopac` pode exibir uma mensagem de uso quando executado sem um
arquivo de entrada. Isso confirma que o executável está disponível. O comando
`IEDA --help` deve listar as opções do programa.

O ambiente `IEDA` deve estar ativado sempre que forem executados os cálculos
do curso:

```bash
conda activate IEDA
```

## VMD 2 sem `sudo`

O VMD 2 está em desenvolvimento e, atualmente, a página oficial disponibiliza
uma versão para Linux 64 bits. O download requer cadastro ou login no site da
Universidade de Illinois.

1. Acesse a [página oficial de download do VMD 2](https://www.ks.uiuc.edu/Research/vmd/vmd2intro/download.html).
2. Baixe o pacote **VMD 2.0 para LINUX**, compatível com Linux 64 bits.
3. Salve o arquivo baixado, normalmente, em `~/Downloads`.

Crie uma pasta para programas instalados pelo usuário e extraia o pacote. No
comando abaixo, substitua `<arquivo-baixado>` pelo nome real do arquivo:

```bash
mkdir -p "$HOME/vmd2"
tar -xf "$HOME/Downloads/<arquivo-baixado>" -C "$HOME/vmd2"
```

Localize o executável instalado e adicione a pasta correspondente ao `PATH`.

```bash
VMD2_BIN="$(find "$HOME/vmd2" -type f -name vmd2 -perm -u+x -print -quit)"
test -n "$VMD2_BIN" || { echo "Executável vmd2 não encontrado" >&2; return 1 2>/dev/null || exit 1; }
echo "export PATH=\"$(dirname "$VMD2_BIN"):\$PATH\"" >> "$HOME/.bashrc"
source "$HOME/.bashrc"
```

```bash
vmd2
```

### Abrir arquivos do curso

Com o ambiente Conda ativado, o VMD pode ser iniciado a partir da pasta que
contém um arquivo PDB:

```bash
conda activate IEDA
vmd2 arquivo.pdb
```

O VMD 2 é uma versão alpha/beta em desenvolvimento. Para obter informações
atualizadas sobre versões e requisitos, consulte a [página oficial do
VMD 2](https://www.ks.uiuc.edu/Research/vmd/vmd2intro/).
