from flask import Blueprint, render_template, redirect, request
from tiendita.modulos.puestos.model.puestos import Puesto
from tiendita.modulos.empleados.models.empleados import Empleado
from tiendita.modulos import db

bp_puestos = Blueprint("puestos", __name__)


@bp_puestos.route('/puestos')
def puestos():
    # for clave,valor in EMPLEADOS.items():
    #   print(f"{clave}>{valor}")
    cdx = {
        "puestos": Puesto.query.all()
    }
    return render_template("puestos/puestos.html",cdx=cdx)


@bp_puestos.route('/puesto/baja/<int:id>', methods =['GET','POST'])
def baja(id):
    if request.method=='GET':
        cdx = {
            'tipo': 'baja',
            'puestos': Puesto.query.get({'id':id})
        }
        return render_template("/puestos/ABC_puestos.html",cdx=cdx)
    elif request.method == 'POST':
        #del(EMPLEADOS[id])
        e = Puesto.query.get({'id':id})
        if e:
            db.session.delete(e)
            db.session.commit()
        return redirect("/puestos")
    else:
        return "ERROR"


@bp_puestos.route('/puesto/cambio/<int:id>', methods =['GET','POST'])
def cambio(id):
    if request.method=='GET':
        cdx = {
            'tipo': 'cambio',
            'puestos': Puesto.query.get({'id':id})
        }
        return render_template("/puestos/ABC_puestos.html",cdx=cdx)
    elif request.method == 'POST':
        e=Puesto.query.get({'id':id})
        if e:
            e.nombre=request.form.get("nombre")
            e.apellido = request.form.get("apellido")
            sexo= request.form.get("sexo")
            if sexo == '1':
                e.sexo='H'
            elif sexo == '2':
                e.sexo='M'
            else:
                e.sexo='Decepticon'
            e.puesto = request.form.get("puesto")
            e.edad=request.form.get("edad")
            salario = request.form.get("salario")
            salario = salario.replace('$','')
            salario = salario.replace(',', '')
            e.salario =float(salario)
            e.comentarios = request.form.get("comentarios")
            db.session.add(e)
            db.session.commit()

        '''EMPLEADOS[id]['nombre'] = request.form.get("nombre")
        EMPLEADOS[id]['apellido'] = request.form.get("apellido")
        EMPLEADOS[id]['sexo']= request.form.get("sexo")
        EMPLEADOS[id]['edad'] = request.form.get("edad")
        EMPLEADOS[id]['Puesto'] = request.form.get("Puesto")
        salario=request.form.get("Salario")
        salario= salario.replace('$','')
        salario= salario.replace(',','')
        EMPLEADOS[id]['Salario'] = float(salario)
        EMPLEADOS[id]['comentarios'] = request.form.get("comentarios")'''
        return redirect("/empleados")
    else:
        return "ERROR"


@bp_puestos.route('/puestos/nuevo', methods=['GET', 'POST'])
def alta():
    if request.method == 'GET':
        cdx = {
            'tipo': 'alta',
            'empleados': Empleado.query.all()
        }
        return render_template("/puestos/ABC_puestos.html", cdx=cdx)
    elif request.method == 'POST':
        nombre = request.form.get("nombre")
        empleado = int(request.form.get("empleado"))
        empleado = Empleado.query.get({'id': empleado})
        puesto = Puesto(
            puesto=nombre,
            empleado=empleado
        )
        db.session.add(puesto)
        db.session.commit()
        return redirect('/puestos')