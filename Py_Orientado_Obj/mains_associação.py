from associação import Escritor
from associação import Caneta
from associação import Marquina_de_escrever


escritor = Escritor("Daniel")
caneta = Caneta("Bic")
maquina = Marquina_de_escrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()