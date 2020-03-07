<monsters_list>
    <div class="text-center">
      <h1>Click on a name for more info</h1>
    </div>
 <div class="container">
    <div class="d-flex justify-content-center">
    <table class="table text-center table-striped table-dark w-25">
   <thead>
     <tr>
       <th scope="col">Name</th>
     </tr>
   </thead>
   <tbody>
     <tr each='{monster in monsters}'>
         <td><a href="/monsters/{monster.id}">{monster.monsterName}</a></td>
     </tr>
   </tbody>
   </table>
   </div>
  </div>
    <script>
     var self = this;
     self.monster = {}
     self.on('mount', function(){
         get_mon_list();
     })
     var get_mon_list = function(){
         CLIENT.api.base_mon()
           .done(function(monsters){
               self.monsters = monsters
            })
            .fail(function(error){
               console.log("Errors == " + error)
             })
             .always(function(){
                self.update()
             })
        }
    </script>
    <style>
        .monster-container {
          background-color: #000;
          padding: 50px 0 0 0;
          margin-top: 15px;
        }
    </style>
</monsters_list>