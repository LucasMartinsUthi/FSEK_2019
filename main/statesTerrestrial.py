from classRobot import Robot 

r = Robot(name="Robot", radius="10", state="0", robot_type="terrestrial")
r.debug()


while True:
    if r.state == "0": #Localização
        #r.searchTrackLimits
            #while True
            #conjunto de funções
            
        #quando tiver sucesso
        r.debug()
        r.state = "1";

    elif r.state == "1":#Aprender Cores
        #funções de odometria para se locomover e achar as cores
        #ao aprender as cores vai para uma posição designada
        #muda de estado
        r.debug()
        r.state = "2";

    elif r.state == "2":#Esperar Ordem
        #fica em loop ouvindo a comunicação bluethoot
        #seta dados das informações

        #Pegar Tubo
        #ou
        #Finalizar

        r.debug()
        r.state = "3";

    elif r.state == "3":#Pegar Tubo
        #Verificar varáveis de mapeamento cor
        #ir até local e obter o tubo
        #com sucesso mudar de estado
        r.debug()
        r.state = "4";

    elif r.state == "4":#Entregar Tubo
        #vai até o local de entrega
        #responde com o sucesso da ordem

        #volta para o estado de espera de ordem
        break
        
    elif r.state == "5":#Finalizar
        #sinaliza finalização da competição
        break


print "Final da Execução"
