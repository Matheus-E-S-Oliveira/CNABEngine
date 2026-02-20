import os
from typing import Any
from flask import Flask, Response, redirect, render_template, request, url_for, session
from cnabengine.core.validators import validate_file
from cnabengine.utils.enums import FileType
from cnabengine.layouts.cnab400.cnab400_shipment import CNAB400Shipment
from cnabengine.layouts.cnab400.cnab400_return import CNAB400Return
from datetime import datetime


app = Flask(__name__)
app.secret_key = "dev-secret-key"

UPLOAD_FOLDER = "temp"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def group_errors(errors):
    grouped = [] 
    context_map = {} 

    for error in errors:
        if "] " in error:
            context, message = error.split("] ", 1)
            context += "]"
        else:
            context = "Geral"
            message = error

        if context not in context_map:
            context_map[context] = []
            grouped.append((context, context_map[context]))

        context_map[context].append(message)

    return grouped

def show_summary(context: dict[str, Any]) -> None:
    context["show_result"] = True


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        file = request.files.get("file")

        if not file or file.filename == "":
            session["error"] = "Selecione um arquivo."
            return redirect(url_for("index"))

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        try:
            validation_date = datetime.now().strftime("%d/%m/%Y %H:%M")
            lines, extension = validate_file(file_path)

            if extension.lower() == FileType.REM.value:
                file_obj = CNAB400Shipment(lines)
                errors = file_obj.validate()

            elif extension.lower() == FileType.RET.value:
                file_obj = CNAB400Return(lines)
                errors = file_obj.validate()
            else:
                session["error"] = "Extensão inválida."
                return redirect(url_for("index"))

            session["validation_result"] = {
                "file_name": file.filename,
                "total_lines": len(lines),
                "total_errors": len(errors),
                "file_type": extension.upper(),
                "validation_date": validation_date,
                "grouped_errors": group_errors(errors) if errors else None,
                "success": not errors,
            }

            return redirect(url_for("index"))

        except Exception as e:
            session["error"] = str(e)
            return redirect(url_for("index"))

    result = session.get("validation_result")

    context = {
        "result": result,
        "error": session.pop("error", None),
        "show_result": result is not None,
    }

    return render_template("index.html", **context)

@app.route("/export")
def export():
    result = session.get("validation_result")

    if not result:
        return redirect(url_for("index"))

    content = []
    content.append(f"Arquivo: {result['file_name']}")
    content.append(f"Tipo: {result['file_type']}")
    content.append(f"Data: {result['validation_date']}")
    content.append(f"Total de Linhas: {result['total_lines']}")
    content.append(f"Total de Erros: {result['total_errors']}")
    content.append("\nErros:\n")

    if result["grouped_errors"]:
        for group, errors in result["grouped_errors"].items():
            content.append(group)
            for err in errors:
                content.append(f"  - {err}")
            content.append("")

    response_text = "\n".join(content)

    return Response(
        response_text,
        mimetype="text/plain",
        headers={
            "Content-Disposition": f"attachment; filename=validacao_{result['file_name']}.txt"
        },
    )
    
@app.route("/clear")
def clear():
    session.pop("validation_result", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
