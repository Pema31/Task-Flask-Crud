from flask import Flask, request, jsonify
from Models.task import Task
app = Flask(__name__)

#CRUD(Creat, Read, Update and Delete -> Criar, ler, atualizar e deletar)

tasks = []
task_id_control = 1
@app.route('/Tasks', methods=['POST'])
def creat_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id = task_id_control, title=data['title'], description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({'message': 'Nova tarefa adicionada com sucesso!'})

@app.route('/Tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
                "Tasks": task_list,
                "Total_tasks": len(task_list)
            }   
    return jsonify(output)
@app.route("/Tasks/<int:id>", methods=['GET'])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    
    return jsonify({"message": "Não foi possivel encontrar a atividade!"}), 404 

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):

    task = None
    for t in tasks:
        if t.id == id:
            task = t

    print(task)
    if task == None:
        return jsonify({"message": "Não foi possovel encontrar a atividade!"}), 404
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({"message": "Atividade atualizada com sucesso!"})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break

    if task == None:
        return jsonify({"message": "Não foi possivel encontrar a atividade"}), 404
    
    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso!"})
 
if __name__ == "__main__":
    app.run(debug=True)