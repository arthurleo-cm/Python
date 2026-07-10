# `def` é como definimos funções em Python
#primeira função aprendendo com o hackthebox
def convite(mãe , pai, criança, professor, evento):

    # Notice here the use of a multi-line format-string: f''' text here '''
    texto_simple = f'''
Prezados {mãe} e {pai}.
{professor} e eu adoraríamos ver vocês dois, bem como {criança} em nosso {evento} amanhã a noite. 

Atenciosamente,
Principal G. Sturgis.
'''
    # Print output
    print(texto_simple)

# Call function
#chamada da função que define ali em cima
convite(mãe='Karen', pai='Fernando', criança='Enzo', professor='Laura', evento='Festa da pizza')
