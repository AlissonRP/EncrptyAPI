import time
import json
from loguru import logger
from service.constants import mensagens
import pandas as pd
import string 
import random


class LowerService():

    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_SERVICO)
        self.load_servico()

    def load_servico(self):
        """"
        Carrega o servico
        """
    def make_encryp(self, texts):
        my_string = "".join(texts["textoMensagem"])

        my_string = my_string.lower()

        trans = my_string.maketrans("aiuoç", "0468@")
        new_my_string = my_string.translate(trans)

        trans = my_string.maketrans("e", random.sample(["&", "$"], 1)[0])
        new_my_string = new_my_string.translate(trans)


    
        alphabet = string.ascii_lowercase
        move_alphabet = alphabet[7:] + alphabet[:7]

    #
        trans_alphabet = my_string.maketrans(alphabet, move_alphabet)

        new_my_string = new_my_string.translate(trans_alphabet)

        trans_alphabet = my_string.maketrans("aemptr", "AEMPTR")

        new_my_string = new_my_string.translate(trans_alphabet)


    #
        new_my_string = new_my_string.replace(",", "#") + "#"

        return new_my_string


    def executar_rest(self, texts):
        response = {}

        logger.debug(mensagens.INICIO_PREDICT)
        start_time = time.time()

        response_predicts =  self.make_encryp(texts)

        logger.debug(mensagens.FIM_PREDICT)
        logger.debug(f"Fim de todas as predições em {time.time()-start_time}")

        df_response = pd.DataFrame(texts, columns=['textoMensagem'])
        df_response['predict'] = response_predicts

        df_response = df_response.drop(columns=['textoMensagem'])

        response = {
                     "listafrase": json.loads(df_response.to_json(
                                                                            orient='records', force_ascii=False))}

        return response

    