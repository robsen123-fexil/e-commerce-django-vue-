<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>shopping</strong></router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu"></a>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </div>
      <div class="navbar-menu" id="navbar-menu">
        <div class="navbar-end">
          <router-link to="/Summer" class="navbar-item">Summer</router-link>
          <router-link to="/Winter" class="navbar-item">Winter</router-link>
        </div>
        <div class="navbar-item">
          <div class="buttons">
            <router-link to="/Log-in" class="button is-light">Log-in</router-link>
            <router-link to="/cart" class="button is-success">
              <span class="icon"><i class="fas fa-shopping-cart"></i></span>
              <span>Cart</span>
            </router-link>
          </div>
        </div>
      </div>
    </nav>
    <section class="section">
      <router-view></router-view>
    </section>
    <footer class="footer">
      <p class="has-text-centered">Copyright 2020</p>
    </footer>
  </div>
</template>

<style lang="scss">
@import '../node_modules/bulma';
</style>
