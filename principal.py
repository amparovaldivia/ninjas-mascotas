from  ninja import Ninja
from mascota import Mascota
from gatos import Gato

nombre='katalina'
mascota=Mascota('atum','gato','pan',100,100)
tipo='gato'
katalina=Ninja(nombre,'saavedra',mascota,'pan','pelet')
katalina= katalina.banar().caminar().comer()
mascota=Mascota.jugar(mascota).sonido().comer()
gato=Gato('atum','pan',10,10,5)
gato.porte()