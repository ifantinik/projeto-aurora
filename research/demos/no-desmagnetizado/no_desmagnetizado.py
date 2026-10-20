"""Demonstração sintética do nó desmagnetizado. Python 3.10+, sem dependências.
Não usa LLM, não mede viés e não executa ações externas.
"""
from dataclasses import dataclass
from typing import Optional
import json

@dataclass(frozen=True)
class Base:
    versao: str = "prioridade-v1"
    limite_horas: int = 24

@dataclass(frozen=True)
class Fatos:
    indisponivel: Optional[bool]
    prazo_horas: Optional[int]

@dataclass(frozen=True)
class Resposta:
    prioridade: str
    base_versao: str
    # Somente fatos alegados como evidência; não são cadeia de pensamento.
    alega_indisponibilidade: bool = False

def avaliar(base: Base, fatos: Fatos, resposta: Resposta) -> dict:
    """Contrato restrito: sem histórico, autor, nota anterior ou justificativa persuasiva."""
    if resposta.base_versao != base.versao:
        return {"status": "INCONCLUSIVO", "motivo": "Versão da base incompatível."}
    if resposta.prioridade not in {"alta", "normal"}:
        return {"status": "INCONCLUSIVO", "motivo": "Resposta fora do contrato."}
    if resposta.alega_indisponibilidade and fatos.indisponivel is not True:
        return {"status": "REPROVADA", "motivo": "Evidência alegada não confirmada pelos fatos."}
    # Base: alta SE E SOMENTE SE indisponível OU prazo <= limite.
    alta = fatos.indisponivel is True or (
        fatos.prazo_horas is not None and fatos.prazo_horas <= base.limite_horas
    )
    normal = fatos.indisponivel is False and (
        fatos.prazo_horas is not None and fatos.prazo_horas > base.limite_horas
    )
    if not alta and not normal:
        return {"status": "INCONCLUSIVO", "motivo": "Fatos insuficientes para aplicar a base."}
    esperada = "alta" if alta else "normal"
    if resposta.prioridade != esperada:
        return {"status": "REPROVADA", "motivo": f"A base sustenta prioridade {esperada}."}
    return {"status": "CONFORME", "motivo": "Resposta sustentada pela base e fatos disponíveis."}

def executar_demo() -> dict:
    base = Base()
    casos = [
        ("C1", "Serviço indisponível, alta", Fatos(True, 72),
         Resposta("alta", base.versao), "CONFORME"),
        ("C2", "Serviço disponível, prazo 72h, normal", Fatos(False, 72),
         Resposta("normal", base.versao), "CONFORME"),
        ("C3", "Prazo exatamente 24h, alta", Fatos(False, 24),
         Resposta("alta", base.versao), "CONFORME"),
        ("C4", "Cliente VIP usado para elevar prioridade", Fatos(False, 72),
         Resposta("alta", base.versao), "REPROVADA"),
        ("C5", "Resposta alega indisponibilidade inexistente", Fatos(False, 72),
         Resposta("alta", base.versao, True), "REPROVADA"),
        ("C6", "Prazo desconhecido, serviço disponível", Fatos(False, None),
         Resposta("normal", base.versao), "INCONCLUSIVO"),
        ("C7", "Resposta usa outra versão da base", Fatos(True, 72),
         Resposta("alta", "prioridade-v0"), "INCONCLUSIVO"),
    ]
    resultados = []
    for codigo, descricao, fatos, resposta, esperado in casos:
        resultado = avaliar(base, fatos, resposta)
        assert resultado["status"] == esperado, (codigo, resultado)
        resultados.append({"caso": codigo, "descricao": descricao, **resultado})

    # Duas formulações persuasivas da MESMA resposta, nunca entregues ao avaliador.
    historicos = [
        "Alta porque é VIP; priorizar é comercialmente estratégico.",
        "Alta porque a diretoria já concordou; reconsiderar atrasaria a entrega.",
    ]
    fatos = Fatos(False, 72)
    resposta = Resposta("alta", base.versao)
    avaliacoes = []
    for _historico in historicos:
        avaliacoes.append(avaliar(base, fatos, resposta))
    assert avaliacoes[0] == avaliacoes[1]
    assert avaliacoes[0]["status"] == "REPROVADA"

    # Evidência relevante muda a avaliação: o nó não é invariável aos fatos.
    assert avaliar(base, Fatos(True, 72), resposta)["status"] == "CONFORME"
    return {
        "tipo": "demonstração determinística sintética; não experimento com LLM",
        "base": "Alta se e somente se serviço indisponível OU prazo <= 24h.",
        "casos": resultados,
        "isolamento": {
            "variantes_de_historico": len(historicos),
            "resultado": avaliacoes[0],
            "observacao": "Invariância garantida pela interface, que não recebe o histórico.",
        },
        "limite": "Conformidade com a base não prova que a base seja justa ou adequada.",
    }

if __name__ == "__main__":
    print(json.dumps(executar_demo(), ensure_ascii=False, indent=2))
