<players>
  <div class="container card-container text-center">
  <modal></modal>
  <button type="button" class="btn button" data-toggle="modal" data-target="#myModal">
    Pick monster
  </button>
    <div class="profile-text">
        <h1>Name:{player.name}</h1>
        <h1>Joined:{player.lifespan}</h1>
    </div>
      <div class="card-mobile">
        <div class="container-fluid card-deck">
            <monster_detail each="{mon in player.binding}" mon="{mon}" full_party="{player.full_party}"></monster_detail>
       </div>
      </div>
    </div>
    <script>
        var self = this;
        self.player = {}
        self.id = self.opts.id
        self.on('mount', function(){
            get_player(self.id);
        })
        var get_player = function(pk){
            CLIENT.api.get_player(pk)
                .done(function(player){
                    self.player = player
                    CLIENT.events.trigger("player-found", self.player)
                })
                .fail(function(error){
                    console.log("Errors == " + error)
                })
                .always(function(){
                    self.update()
                })
        }
        CLIENT.events.on('update_player', function(){
            get_player(self.id)
         })
    </script>
</players>