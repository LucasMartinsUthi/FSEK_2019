from classRobot import Robot 

r = Robot(name="Robot", radius="10", state="0", robot_type="aquatic")
r.debug()


while True:
    if r.state == "0": #Localização
        #r.searchTrackLimits
            #while True
            #conjunto de funções
            
        #quando tiver sucesso

    elif r.state == "1":#Mapear Buracos
        #usar sensores para localizar os buracos
        #mapear suas posições


    elif r.state == "2":#Localizar Buraco
        #usar a variavel de mapeamento para localizar o buraco mais proximo
        #ir até o local e verificar sua existencia
        
        #sucesso enviar ordem
        #else ir para o proximo
        #quando nenhum for encontrado enviar ordem de finalização

    elif r.state == "3":#Enviar Ordem
        #Se comunica com o robô terrestre

    elif r.state == "4":#Pegar Tubo
        #vai até o local de encontro
        #espera resposta
        #pegar o tubo
        
    elif r.state == "5":#Preenchendo Buraco
        #Deve ir até o buraco 
        #Posicionar o tubo
        #voltar ao estado de localizar buraco

