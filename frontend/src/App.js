import './App.css';

import { useState, useEffect } from 'react';
import { BsTrash, BsBookmarkCheck, BsBookmarkCheckFill } from 'react-icons/bs'

const API = 'http://127.0.0.1:8000/v1/'

function App() {
  return (
    <div className="App">
      <div className='nexus-header'>
        <h1>Nexus Match</h1>
      </div>

      <div className='main'>
        <div className='modal-login modal-gamer'>
          <h2>Login</h2>
          <div className='container-input'>
            <input className='input-gamer input'></input>
            <input className='input-gamer input'></input>
          </div>
          <div className='options'>
            <span>esqueceu a senha?</span>
            <span>cadastre-se</span>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
