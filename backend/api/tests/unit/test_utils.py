from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from api.utils import verify_video_file_extension_is_ok

class TestUtilsVideoExtension(TestCase):

    def test_com_extensao_valida_deve_retornar_true(self):
        """
        Caso de Teste (Caminho Feliz): 
        Verifica se um arquivo com uma extensão de vídeo válida (.mp4) retorna True.
        """
        video_file = SimpleUploadedFile("video_teste.mp4", b"file_content")

        resultado = verify_video_file_extension_is_ok(video_file)

        self.assertTrue(resultado)

    def test_com_extensao_invalida_deve_retornar_false(self):
        """
        Caso de Teste (Caminho Triste): 
        Verifica se um arquivo de texto (.txt) retorna False.
        """
        text_file = SimpleUploadedFile("documento.txt", b"file_content")

        resultado = verify_video_file_extension_is_ok(text_file)

        self.assertFalse(resultado)

    def test_com_extensao_maiuscula_deve_retornar_true(self):
        """
        Caso de Teste (Borda): 
        Verifica se a função ignora o case (maiúsculas/minúsculas) da extensão.
        """
        video_file_upper = SimpleUploadedFile("video_upper.MP4", b"file_content")

        resultado = verify_video_file_extension_is_ok(video_file_upper)

        self.assertTrue(resultado)

    def test_sem_extensao_deve_retornar_false(self):
        """
        Caso de Teste (Borda): 
        Verifica o comportamento com um arquivo sem extensão.
        """
        file_no_ext = SimpleUploadedFile("arquivo_sem_extensao", b"file_content")

        resultado = verify_video_file_extension_is_ok(file_no_ext)

        self.assertFalse(resultado)