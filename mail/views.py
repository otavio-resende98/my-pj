from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives


# Create your views here.
def miss_metting(request):
	subject, from_email, to = 'Ausência reunião.', 'ericsantosfaria29@gmail.com', 'isaiasbd@hotmail.com'
	text_content = 'Olá, \
					Identificamos que você não compareceu a reunião essa semana, portanto, conforme estipulado pelo Programa de Controle Disciplinar em seu art. 6°, você tem até 48 horas contando a partir do momento de recebimento dessa mensagem para enviar um e-mail para a Diretoria de Processos Internos contendo: \
					\
					I - Data de ocorrência do ato faltoso;\
					II - Breve descrição do ocorrido;\
					III - Justificativa com documento que comprove o motivo da falta. \
					\
					Se essa mensagem não for respondida em tempo hábil, poderá vir a ser computada uma advertência moderada como determinado no Programa de Controle Disciplinar em seu art. 2º, II, "c". \
					Lembramos que esta advertência possui duração de 6 meses em seu registro, sendo expirada após esse prazo.\
					\
					Quaisquer dúvidas, procure a diretoria de Processos Internos.\
					\
					Atenciosamente,\
					Diretoria de Processos Internos'
	html_content = '<p>Olá,</p> \
					<p>Identificamos que você não compareceu a reunião essa semana, portanto, conforme estipulado pelo Programa de Controle Disciplinar em seu art. 6°, você tem até 48 horas contando a partir do momento de recebimento dessa mensagem para enviar um e-mail para a Diretoria de Processos Internos contendo:</p> \
					<p></p>\
					<i><p>I - Data de ocorrência do ato faltoso;</p>\
					<p>II - Breve descrição do ocorrido;</p>\
					<p>III - Justificativa com documento que comprove o motivo da falta.</p></i>\
					<p></p>\
					<p>Se essa mensagem não for respondida em tempo hábil, poderá vir a ser computada uma advertência moderada como determinado no Programa de Controle Disciplinar em seu art. 2º, II, "c".</p> \
					<p>Lembramos que esta advertência possui duração de 6 meses em seu registro, sendo expirada após esse prazo.</p>\
					<p></p>\
					<p>Quaisquer dúvidas, procure a diretoria de Processos Internos.</p>\
					<p></p>\
					<strong><p>Atenciosamente,</p>\
					<p>Diretoria de Processos Internos</p></strong>'
	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	msg.send()
	return render(request, 'mail/index.html')

def miss_time(request):
	subject, from_email, to = 'Ausência ao horário de sala.', 'ericsantosfaria29@gmail.com', 'isaiasbd@hotmail.com'
	text_content = 'Olá, \
					Identificamos que você não compareceu ao horário de sala essa semana, portanto, conforme estipulado pelo Programa de Controle Disciplinar em seu art. 6°, você tem até 48 horas contando a partir do momento de recebimento dessa mensagem para enviar um e-mail para a Diretoria de Processos Internos contendo: \
					\
					I - Data de ocorrência do ato faltoso;\
					II - Breve descrição do ocorrido;\
					III - Justificativa com documento que comprove o motivo da falta. \
					\
					Se essa mensagem não for respondida em tempo hábil, poderá vir a ser computada uma advertência moderada como determinado no Programa de Controle Disciplinar em seu art. 2º, II, "c". \
					Lembramos que esta advertência possui duração de 6 meses em seu registro, sendo expirada após esse prazo.\
					\
					Quaisquer dúvidas, procure a diretoria de Processos Internos.\
					\
					Atenciosamente,\
					Diretoria de Processos Internos'
	html_content = '<p>Olá,</p> \
					<p>Identificamos que você não compareceu ao horário de sala essa semana, portanto, conforme estipulado pelo Programa de Controle Disciplinar em seu art. 6°, você tem até 48 horas contando a partir do momento de recebimento dessa mensagem para enviar um e-mail para a Diretoria de Processos Internos contendo:</p> \
					<p></p>\
					<i><p>I - Data de ocorrência do ato faltoso;</p>\
					<p>II - Breve descrição do ocorrido;</p>\
					<p>III - Justificativa com documento que comprove o motivo da falta.</p></i>\
					<p></p>\
					<p>Se essa mensagem não for respondida em tempo hábil, poderá vir a ser computada uma advertência moderada como determinado no Programa de Controle Disciplinar em seu art. 2º, II, "c".</p> \
					<p>Lembramos que esta advertência possui duração de 6 meses em seu registro, sendo expirada após esse prazo.</p>\
					<p></p>\
					<p>Quaisquer dúvidas, procure a diretoria de Processos Internos.</p>\
					<p></p>\
					<strong><p>Atenciosamente,</p>\
					<p>Diretoria de Processos Internos</p></strong>'
	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	msg.send()
	return render(request, 'mail/index.html')

