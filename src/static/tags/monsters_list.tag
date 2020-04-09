<monsters_list>
<div class="container monster-container bg-dark">
    <div class="text-center text-white">
      <h1>Click on a name for more info</h1>
    </div>
    <div class="d-flex justify-content-center">
    <table class="table text-center table-hover table-bordered table-info table-margin">
   <thead class="thead-light">
     <tr>
       <th scope="col">Name</th>
       <th scope="col">Family</th>
       <th scope="col">Element</th>
       <th scope="col">Description</th>
     </tr>
   </thead>
   <tbody id="table">
     <tr each='{monster in monsters}' role="button" data-href="/monsters/{monster.id}">
         <td><a class="text-dark">{monster.monsterName}</a></td>
         <td><a>{monster.family}</a></td>
         <td><a>{monster.element}</a></td>
         <td><a>{monster.description}</a></td>
     </tr>
   </tbody>
   </table>
   </div>
 </div>
    <script>
     var self = this;
     self.monsters = {}
     self.on('mount', function(){
         get_mon_list();
     })

      $(function(){
        $(".table").on("click", "tr[role=\"button\"]", function (e) {
          window.location = $(this).data("href");
        });
      });

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
          padding: 35px 50px 35px 50px;
          margin-top: 15px;
        }
        .table-margin {
          margin-top: 40px;
        ]
    </style>
</monsters_list>