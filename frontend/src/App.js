import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [alunos, setAlunos] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/alunos/")
      .then(res => res.json())
      .then(data => setAlunos(data));
  }, []);

  const deletarAluno = async (id) => {
    const resposta = await fetch(`http://localhost:8000/alunos/${id}`, {
      method: 'DELETE'
    });

    if (resposta.ok) {
      setAlunos(alunos.filter(aluno => aluno.id !== id));
    } else {
      alert("Erro ao deletar aluno");
    }
  };

  return (
    <div className="container">
      <h1>Lista de Alunos</h1>
      <ul>
        {alunos.map(aluno => (
          <li key={aluno.id}>
            {aluno.nome} - {aluno.email}
            <button onClick={() => deletarAluno(aluno.id)}>Deletar</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
