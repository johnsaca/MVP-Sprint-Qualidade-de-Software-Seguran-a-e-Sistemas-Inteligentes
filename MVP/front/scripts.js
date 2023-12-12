/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'http://127.0.0.1:5000/pacientes';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.pacientes.forEach(item => insertList(item.name,
        item.age,
        item.sex,
        item.chol,
        item.blup,
        item.bllow,
        item.rate,
        item.dia,
        item.fam,
        item.smok,
        item.obes,
        item.alco,
        item.exer,
        item.diet,
        item.prev,
        item.medi,
        item.stress,
        item.seden,
        item.income,
        item.bmi,
        item.trigly,
        item.activity,
        item.sleep,
        item.outcome
      ))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Chamada da função para carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList()




/*
  --------------------------------------------------------------------------------------
  Função para colocar um item na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
const postItem = async (inputPatient, inputAge, inputSex, inputChol, inputBlup, inputBllow,
  inputRate, inputDia, inputFam, inputSmok, inputObes, inputAlco, inputExer, inputDiet, inputPrev,
  inputMedi, inputStress, inputSeden, inputIncome, inputBMI, inputTrigly, inputActivity, inputSleep) => {

  const formData = new FormData();
  formData.append('name', inputPatient);
  formData.append('age', inputAge);
  formData.append('sex', inputSex);
  formData.append('chol', inputChol);
  formData.append('blup', inputBlup);
  formData.append('bllow', inputBllow);
  formData.append('rate', inputRate);
  formData.append('dia', inputDia);
  formData.append('fam', inputFam);
  formData.append('smok', inputSmok);
  formData.append('obes', inputObes);
  formData.append('alco', inputAlco);
  formData.append('exer', inputExer);
  formData.append('diet', inputDiet);
  formData.append('prev', inputPrev);
  formData.append('medi', inputMedi);
  formData.append('stress', inputStress);
  formData.append('seden', inputSeden);
  formData.append('income', inputIncome);
  formData.append('bmi', inputBMI);
  formData.append('trigly', inputTrigly);
  formData.append('activity', inputActivity);
  formData.append('sleep', inputSleep);

  let url = 'http://127.0.0.1:5000/paciente';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para criar um botão close para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertDeleteButton = (parent) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  parent.appendChild(span);
}

/*
  --------------------------------------------------------------------------------------
  Função para remover um item da lista de acordo com o click no botão close
  --------------------------------------------------------------------------------------
*/
const removeElement = () => {
  let close = document.getElementsByClassName("close");
  var table = document.getElementById('myTable');
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const nomeItem = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Você tem certeza?")) {
        div.remove()
        deleteItem(nomeItem)
        alert("Removido!")
      }
    }
  }
}

/*
  --------------------------------------------------------------------------------------
  Função para deletar um item da lista do servidor via requisição DELETE
  --------------------------------------------------------------------------------------
*/
const deleteItem = (item) => {
  console.log(item)
  let url = 'http://127.0.0.1:5000/paciente?name=' + item;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo item com nome, quantidade e valor 
  --------------------------------------------------------------------------------------
*/
const newItem = async () => {
  let inputPatient = document.getElementById("newInput").value;
  let inputAge = document.getElementById("newAge").value;
  let inputSex = document.getElementById("newSex").value;
  let inputChol = document.getElementById("newChol").value;
  let inputBlup = document.getElementById("newBlup").value;
  let inputBllow = document.getElementById("newBlup").value;
  let inputRate = document.getElementById("newRate").value;
  let inputDia = document.getElementById("newDia").value;
  let inputFam = document.getElementById("newFam").value;
  let inputSmok = document.getElementById("newSmok").value;
  let inputObes = document.getElementById("newObes").value;
  let inputAlco = document.getElementById("newAlco").value;
  let inputExer = document.getElementById("newExer").value;
  let inputDiet = document.getElementById("newDiet").value;
  let inputPrev = document.getElementById("newPrev").value;
  let inputMedi = document.getElementById("newMedi").value;
  let inputStress = document.getElementById("newStress").value;
  let inputSeden = document.getElementById("newSeden").value;
  let inputIncome = document.getElementById("newIncome").value;
  let inputBMI = document.getElementById("newBMI").value;
  let inputTrigly = document.getElementById("newTrigly").value;
  let inputActivity = document.getElementById("newActivity").value;
  let inputSleep = document.getElementById("newSleep").value;

  // Verifique se o nome do produto já existe antes de adicionar
  const checkUrl = `http://127.0.0.1:5000/pacientes?nome=${inputPatient}`;
  fetch(checkUrl, {
    method: 'get'
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.pacientes && data.pacientes.some(item => item.name === inputPatient)) {
        alert("O paciente já está cadastrado.\nCadastre o paciente com um nome diferente ou atualize o existente.");
      } else if (inputPatient === '') {
        alert("O nome do paciente não pode ser vazio!");
      } else if (isNaN(inputPatient) || isNaN(inputAge) || isNaN(inputSex) || isNaN(inputChol) || isNaN(inputBlup) || isNaN(inputBllow) ||
        isNaN(inputRate) || isNaN(inputDia) || isNaN(inputFam) || isNaN(inputSmok) || isNaN(inputObes) || isNaN(inputAlco) || isNaN(inputExer) || isNaN(inputDiet) || isNaN(inputPrev) ||
        isNaN(inputMedi) || isNaN(inputStress) || isNaN(inputSeden) || isNaN(inputIncome) || isNaN(inputBMI) || isNaN(inputTrigly) || isNaN(inputActivity) || isNaN(inputSleep)) {
        alert("Esse(s) campo(s) precisam ser números!");
      } else {
        insertList(inputPatient, inputAge, inputSex, inputChol, inputBlup, inputBllow,
          inputRate, inputDia, inputFam, inputSmok, inputObes, inputAlco, inputExer, inputDiet, inputPrev,
          inputMedi, inputStress, inputSeden, inputIncome, inputBMI, inputTrigly, inputActivity, inputSleep);
        postItem(inputPatient, inputAge, inputSex, inputChol, inputBlup, inputBllow,
          inputRate, inputDia, inputFam, inputSmok, inputObes, inputAlco, inputExer, inputDiet, inputPrev,
          inputMedi, inputStress, inputSeden, inputIncome, inputBMI, inputTrigly, inputActivity, inputSleep);
        alert("Item adicionado!");
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para inserir items na lista apresentada
  --------------------------------------------------------------------------------------
*/
const insertList = (namePatient, age, sex, chol, blup, bllow, rate, dia, fam, smok, obes, alco, exer, diet, prev,
  medi, stress, seden, income, bmi, trigly, activity, sleep, outcome) => {
  var item = [namePatient, age, sex, chol, blup, bllow, rate, dia, fam, smok, obes, alco, exer, diet, prev,
    medi, stress, seden, income, bmi, trigly, activity, sleep, outcome];
  var table = document.getElementById('myTable');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cell = row.insertCell(i);
    cell.textContent = item[i];
  }

  var deleteCell = row.insertCell(-1);
  insertDeleteButton(deleteCell);


  document.getElementById("newInput").value = "";
  document.getElementById("newInput").value = "";
  document.getElementById("newAge").value = "";
  document.getElementById("newSex").value = "";
  document.getElementById("newChol").value = "";
  document.getElementById("newBlup").value = "";
  document.getElementById("newBlup").value = "";
  document.getElementById("newRate").value = "";
  document.getElementById("newDia").value = "";
  document.getElementById("newFam").value = "";
  document.getElementById("newSmok").value = "";
  document.getElementById("newObes").value = "";
  document.getElementById("newAlco").value = "";
  document.getElementById("newExer").value = "";
  document.getElementById("newDiet").value = "";
  document.getElementById("newPrev").value = "";
  document.getElementById("newMedi").value = "";
  document.getElementById("newStress").value = "";
  document.getElementById("newSeden").value = "";
  document.getElementById("newIncome").value = "";
  document.getElementById("newBMI").value = "";
  document.getElementById("newTrigly").value = "";
  document.getElementById("newActivity").value = "";
  document.getElementById("newSleep").value = "";

  removeElement();
}