from cnabengine.core.validators.core.numeric_validator import NumericValidator
from cnabengine.core.validators.core.alpha_validator import AlphaValidator
from cnabengine.core.validators.core.static_validator import StaticValidator
from cnabengine.core.validators.core.date_validator import DateValidator

# Observações:
# A validação do arquivo de retorno foi feita com base no codígo conforme pedido, como codigo não valida os valores
# no momento esta sendo feita apenas as validações de conversão para valore numéricos e valores de datas
# no caso das strings não esta sendoo feita nehuma validação no momento pois por natureza eles são strings dede o começo
# e não está sendo validação dos valores, pois não e especificado quais campos podem ou não estar vazios e como requerimento
# foi de fazer baseado no codígo do sistema nenhuma validação foi aplicada alem da de checar conversão dos valores
# e além disso não será feita validação do TRILLER pois no sistema não está sendo implementada


def validate_body(details: list[str], errors: list[str]) -> None:

    for i, line in enumerate(details, start=2):
        context = f"BODY LINE {i}"

        if len(line) != 400:
            errors.append(
                f"[{context}]: comprimento inválido. Cada linha do CNAB 400 deve conter exatamente 400 caracteres."
            )
            continue
        
        # Posição 001-001 - Identificação
        NumericValidator.validate_numeric(field=line[0:1], context=context, position="001-001", errors=errors)
        
        # Posição 002-003 - Zeros 1
        NumericValidator.validate_numeric(field=line[1:3], context=context, position="002-003", errors=errors)
        
        # Posição 004-017 - Zeros 2
        NumericValidator.validate_numeric(field=line[3:17], context=context, position="004-017", errors=errors)
        
        # Posição 018-021- Prefixo Agência
        NumericValidator.validate_numeric(field=line[17:21], context=context, position="018-021", errors=errors)
        
        # Posição 022-022 - DV Prefixo Agência
        NumericValidator.validate_numeric(field=line[21:22], context=context, position="022-022", errors=errors)
        
        # Posição 023-030 - Conta Corrente
        NumericValidator.validate_numeric(field=line[22:30], context=context, position="023-030", errors=errors)
        
        # Posição 031-031 - Dv Conta Corrente
        NumericValidator.validate_numeric(field=line[30:31], context=context, position="031-031", errors=errors)
        
        # Posição 032-038 - Número Convênio
        NumericValidator.validate_numeric(field=line[32:38], context=context, position="032-038", errors=errors)
        
        # Posição 039-063 - Número Controle
        AlphaValidator.validate_alpha(field=line[38:63], context=context, position="039-063", errors=errors, fieldName="número controle")
        
        # Posição 064-080 - Nosso Número
        AlphaValidator.validate_alpha(field=line[63:80], context=context, position="064-080", errors=errors, fieldName="nosso número")
        
        # Posição 081-081 - Tipo Cobrança
        NumericValidator.validate_numeric(field=line[80:81], context=context, position="081-081", errors=errors)
        
        # Posição 082-082 - Tipo Cobrança Específico
        NumericValidator.validate_numeric(field=line[81:82], context=context, position="082-082", errors=errors)
        
        # Posição 083-086 - Dias para cáuculo
        NumericValidator.validate_numeric(field=line[82:86], context=context, position="083-086", errors=errors)
        
        # Posição 087-088 - Natureza recebimento
        NumericValidator.validate_numeric(field=line[86:88], context=context, position="087-088", errors=errors) 
        
        # Posição 089-091 - Prefixo Titulo
        # String e o sistema não utiliza esse campo
        
        # Posição 092-094 - Variação Carteira
        NumericValidator.validate_numeric(field=line[91-94], context=context, position="092-094", errors=errors)
        
        # Posição 095-095 - Cota Caução
        NumericValidator.validate_numeric(field=line[94:95], context=context, position="095-095", errors=errors)
        
        # Posição 096-100 - Taxa desconto
        NumericValidator.validate_numeric(field=line[95:100], context=context, position="096-100", errors=errors)
        
        # Posição 101-105 - Taxa IOF
        NumericValidator.validate_numeric(field=line[100:105], context=context, position="101-105", errors=errors)
        
        # Posição 106-106 - Brancos 1
        StaticValidator.validate_field_space(field=line[105:106], context=context, position="106-106", errors=errors)
        
        # Posição 107-108 - Carteira
        AlphaValidator.validate_alpha(field=line[106:108], context=context, position="107-108", errors=errors, fieldName="carteira")
        
        # Posição 109-110 - Comando
        NumericValidator.validate_numeric(field=line[108:110], context=context, position="109-110", errors=errors)
        
        # Posição 111-116 - Data de liquidação
        DateValidator.validate_date_format_ddmmaa(field=line[110:116], context=context, position="111-116", errors=errors)
        
        # Posição 117-126 - Número título
        AlphaValidator.validate_alpha(field=line[116-126], context=context, position="117-126", errors=errors, fieldName="número título")
        
        # Posição 127-146 - Brancos 2
        StaticValidator.validate_field_space(field=line[126:146], context=context, position="127-146", errors=errors)
        
        # Posição 147-152 - Data Vencimento
        DateValidator.validate_date_format_ddmmaa(field=line[146:152], context=context, position="147-152", errors=errors)
        
        # Posição 153-165 - Valor título
        NumericValidator.validate_numeric(field=line[150:165], context=context, position="153-165", errors=errors)
        
        # Posição 166-168 - Código banco recebedor
        NumericValidator.validate_numeric(field=line[165:168], context=context, position="166-168", errors=errors)
        
        # Posição 169-172 - Prefico agência recebedora
        NumericValidator.validate_numeric(field=line[168:172], context=context, position="169-172", errors=errors)
        
        # Posição 173-173 - DV prefixo agencia recebedora
        # String e o sistema não usa
        
        # Posição 174-175 - Especie Titulo
        NumericValidator.validate_numeric(field=line[173:175], context=context, position="174-175", errors=errors)
        
        # Posição 176-181 - Data Credito
        DateValidator.validate_date_format_ddmmaa(field=line[175:181], context=context, position="176-181", errors=errors)
        
        # Posição 182-188 - Valor tarifa
        NumericValidator.validate_numeric(field=line[181:188], context=context, position="182-188", errors=errors)
        
        # Posição 189-201 - Outras despesas
        NumericValidator.validate_numeric(field=line[188:201], context=context, position="189-201", errors=errors)
        
        # Posição 202-214 - Juros Desconto
        NumericValidator.validate_numeric(field=line[201:214], context=context, position="202-214", errors=errors)
        
        # Posição 215-227 - IOF Desconto
        NumericValidator.validate_numeric(field=line[214:227], context=context, position="215-227", errors=errors)
        
        # Posição 228-240 - Valor Abatimento
        NumericValidator.validate_numeric(field=line[227:240], context=context, position="228-240", errors=errors)
        
        # Posição 241-253 - Desconto concedido
        NumericValidator.validate_numeric(field=line[240:253], context=context, position="241-253", errors=errors)
        
        # Posição 254-266 - Valor recebido
        NumericValidator.validate_numeric(field=line[253:266], context=context, position="254-266", errors=errors)
        
        # Posição 267-279 - Juros Mora
        NumericValidator.validate_numeric(field=line[266:279], context=context, position="267-279", errors=errors)
        
        # Posição 280-292 - Outros Recebimentos
        NumericValidator.validate_numeric(field=line[279:292], context=context, position="280-292", errors=errors)
        
        # Posição 293-305 - Abatimento Não aproveitado
        NumericValidator.validate_numeric(field=line[292:305], context=context, position="293-305", errors=errors)
        
        # Posição 306-318 - Valor Lançamento
        NumericValidator.validate_numeric(field=line[305:318], context=context, position="306-318", errors=errors)
        
        # Posição 319-319 - Indica debito credito
        NumericValidator.validate_numeric(field=line[318:319], context=context, position="319-319", errors=errors)
        
        # Posição 320-320 - Indica Valor
        NumericValidator.validate_numeric(field=line[319:320], context=context, position="320-320", errors=errors)
        
        # Posição 321-332 - Valor Ajuste
        NumericValidator.validate_numeric(field=line[320:332], context=context, position="321-332", errors=errors)
        
        # Posição 333-333 - Brnaco 3
        StaticValidator.validate_field_space(field=line[332:333], context=context, position="333-333", errors=errors)
        
        # Posição 334-342 - Brancos 4
        StaticValidator.validate_field_space(field=line[333:342], context=context, position="334-342", errors=errors)
        
        # Posição 343-349 - Zeros 3
        NumericValidator.validate_numeric(field=line[342:349], context=context, position="343-349", errors=errors)
        
        # Posição 350-358 - Zeros 4
        NumericValidator.validate_numeric(field=line[349:358], context=context, position="350-358", errors=errors)
        
        # Posição 359-365 - Zeros 5
        NumericValidator.validate_numeric(field=line[358:365], context=context, position="359-365", errors=errors)
        
        # Posição 366-374 - Zeros 6
        NumericValidator.validate_numeric(field=line[365:374], context=context, position="366-374", errors=errors)
        
        # Posição 375-381 - Zeros 7
        NumericValidator.validate_numeric(field=line[374:381], context=context, position="375-381", errors=errors)
        
        # Posição 382-390 - Zeros 8
        NumericValidator.validate_numeric(field=line[381:390], context=context, position="382-390", errors=errors)
        
        # Posição 391-392 - Brancos 5
        StaticValidator.validate_field_space(field=line[390:392], context=context, position="391-392", errors=errors)
        
        # Posição 393-394 - Canal Pagamento
        NumericValidator.validate_numeric(field=line[392:394], context=context, position="393-394", errors=errors)
        
        # Posição 395-400 - Numero sequencial registro
        NumericValidator.validate_numeric(field=line[394:400], context=context, position="395-400", errors=errors)