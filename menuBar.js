var html = `
    <div class="menu">
      <button
        class="column_1 column btn btn-warning"
        onclick="window.location.href = 'index.html';"
      >
        Home
      </button>
      <button
        class="column_1 column btn btn-primary"
        onclick="window.location.href = 'resume.html';"
      >
        Resume
      </button>
      <button
        class="column_2 column btn btn-secondary"
        onclick="window.location.href = 'portfolio.html';"
      >
        Portfolio
      </button>
      <button
        class="column_3 column btn btn-success"
        onclick="window.location.href = 'contactMe.html';"
      >
        Contact Me
      </button>
    </div>
 
  <style>
    * {
      margin: 0;
      border: 0;
    }
    .menu {
      display: flex;
      flex-grow: initial;
      align-items: center;
      flex-direction: column;
      justify-content: space-evenly;
      background: linear-gradient(to bottom, aqua, #000000);
      height: 100vh;
      width: 15vh;
    }
 
  </style>
`;
document.getElementById("menuBar").innerHTML = html;
