<template>
  <div>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">UrFUbe</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Link</a>
            </li>
            <li class="nav-item">
              <a class="nav-link disabled">Disabled</a>
            </li>
          </ul>
          <form class="d-flex" role="search">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button id="search-button" type="button" class="btn btn-primary">
              <p>Search</p>
            </button>
          </form>
          <div class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Dropdown
            </a>
            <ul class="dropdown-menu">
              <li>
                <button class="dropdown-item btn btn-outline-primary " href="#">Action</button>
              </li>
              <li>
                <button class="dropdown-item btn btn-outline-primary " href="#">Another action</button>
              </li>
              <li>
                <hr class="dropdown-divider">
              </li>
              <li>
                <button class="dropdown-item btn btn-outline-primary " href="#">Something else here</button>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </nav>
    <hr>
  </div>
</template>

<script>
export default {
  name: "Header"
}
</script>

<style scoped>
.dropdown {
  margin-right: 9%;
}

form {
  max-width: 1000px;
  width: 700px;
  height: 40px;
  margin: 10px auto;
}
hr{
  margin: 0px;
}


</style>