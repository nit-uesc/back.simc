"""."""
from zeep import Client

URL = 'http://servicosweb.cnpq.br/srvcurriculo/WSCurriculo?wsdl'
LOCATION = 'http://servicosweb.cnpq.br/srvcurriculo/WSCurriculo'
CPF = '05049164591'
IP = '200.128.66.214'


class Cnpq:
    """."""

    def __init__(self):
        """."""
        self.__client = Client(URL)

        self.__service = self.__client.service
        self.__cnpq_id = None

    def get_cnpq_id(self, cpf):
        """."""
        # getIdentificadorCNPq(cpf=cpf, nomeCompleto='', dataNascimento='')
        # getCurriculoCompactado(id=self.__cnpq_id)
        return None

    def get_compressed_curriculum(self, cpf):
        """."""
        blob = self.__client->getCurriculoCompactado($id);
        $tmp = tmpfile();
        fwrite($tmp, $curriculo_compactado_base64);
        $tmp_meta = stream_get_meta_data($tmp);
        $curriculo = exec("unzip -p ".$tmp_meta['uri']);
        fclose($tmp);    
        return $curriculo;
        # should return the data
        # getCurriculoCompactado(id=self.__cnpq_id)
        return None

    def get_curriculum_update_date(self):
        """."""
        return None
        # getDataAtualizacaoCV(id=self.__cnpq_id)
