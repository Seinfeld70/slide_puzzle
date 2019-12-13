const UIController = (() => {
  const domStr = { grid: '.grid' };

  const addGridChild = (id, i) => {
    const grid = document.querySelector(`${domStr.grid}`);
    const el = document.createElement('div');
    el.classList.add('grid-child');
    el.id = `con-${i}`;
    const img = document.createElement('img');
    img.src = `../images/Layer ${id}.jpg`;
    img.id = `img-${id}`;
    el.appendChild(img);
    grid.appendChild(el);
  };

  function swap(el, from) {
    const elem = document.getElementById(el);
    document.getElementById(`con-${from}`).innerHTML = elem.innerHTML;
    elem.innerHTML = '<img src="../images/Layer 8.jpg" id="8"/>';
  }
  return {
    domStr,
    addGridChild,
    swap
  };
})();

const StateController = (() => {
  state = [];

  const randomlyFill = () => {
    let rN = random();
    while (itemAlreadyExist(state, rN)) rN = random();

    function itemAlreadyExist(arr, item) {
      if (arr.indexOf(item) === -1) {
        arr.push(item);
        return false;
      }
      return true;
    }
  };

  const changeState = (index, value) => {
    state[index] = state[value];
    state[value] = '';
    console.log(state);
  };

  return {
    state,
    randomlyFill,
    changeState
  };
})();

const AppController = (UI, State) => {
  for (let i = 0; i < 8; i++) {
    State.randomlyFill();
    UI.addGridChild(State.state[i], i);
  }
  UI.addGridChild(8, 8);
  State.state.push('');
  document.querySelector(UI.domStr.grid).addEventListener('click', movePieces);

  function movePieces(e) {
    const parEl = e.target.parentElement.id;
    // UI.move(parEl, State.state);
    switch (parEl) {
      case 'con-0':
        if (state[1] === '') {
          State.changeState(1, 0);
          UI.swap(parEl, 1);
        } else if (state[3] === '') {
          State.changeState(3, 0);
          UI.swap(parEl, 3);
        }
        break;
      case 'con-1':
        if (state[0] === '') {
          State.changeState(0, 1);
          UI.swap(parEl, 0);
        } else if (state[2] === '') {
          State.changeState(2, 1);
          UI.swap(parEl, 2);
        } else if (state[4] === '') {
          State.changeState(4, 1);
          UI.swap(parEl, 4);
        }
        break;
      case 'con-2':
        if (state[1] === '') {
          State.changeState(1, 2);
          UI.swap(parEl, 1);
        } else if (state[5] === '') {
          State.changeState(5, 2);
          UI.swap(parEl, 5);
        }
        break;
      case 'con-3':
        if (state[0] === '') {
          State.changeState(0, 3);
          UI.swap(parEl, 0);
        } else if (state[4] === '') {
          State.changeState(4, 3);
          UI.swap(parEl, 4);
        } else if (state[6] === '') {
          State.changeState(6, 3);
          UI.swap(parEl, 6);
        }
        break;
      case 'con-4':
        if (state[5] === '') {
          State.changeState(5, 4);
          UI.swap(parEl, 5);
        } else if (state[1] === '') {
          State.changeState(1, 4);
          UI.swap(parEl, 1);
        } else if (state[3] === '') {
          State.changeState(3, 4);
          UI.swap(parEl, 3);
        } else if (state[7] === '') {
          State.changeState(7, 4);
          UI.swap(parEl, 7);
        }
        break;
      case 'con-5':
        if (state[8] === '') {
          State.changeState(8, 5);
          UI.swap(parEl, 8);
        } else if (state[4] === '') {
          State.changeState(4, 5);
          UI.swap(parEl, 4);
        } else if (state[2] === '') {
          State.changeState(2, 5);
          UI.swap(parEl, 2);
        }
        break;
      case 'con-6':
        if (state[3] === '') {
          State.changeState(3, 6);
          UI.swap(parEl, 3);
        } else if (state[7] === '') {
          State.changeState(7, 6);
          UI.swap(parEl, 7);
        }
        break;
      case 'con-7':
        if (state[8] === '') {
          State.changeState(8, 7);
          UI.swap(parEl, 8);
        } else if (state[6] === '') {
          State.changeState(6, 7);
          UI.swap(parEl, 6);
        } else if (state[4] === '') {
          State.changeState(4, 7);
          UI.swap(parEl, 4);
        }
        break;
      case 'con-8':
        if (state[5] === '') {
          State.changeState(5, 8);
          UI.swap(parEl, 5);
        } else if (state[7] === '') {
          State.changeState(7, 8);
          UI.swap(parEl, 7);
        }
        break;
      default:
        console.log('What was that!');
    }
    checkWin();
  }

  function checkWin() {
    for (let i = 0; i < State.state.length; i++) {
      if (i !== State.state[i]) break;
      else if (i === State.state.length - 1) alert("You've won");
    }
  }
};

AppController(UIController, StateController);

function random() {
  return Math.floor(Math.random() * 8);
}
