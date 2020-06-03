<monsters_list>
<div class="container">
    <div class="text-center text text-dark">
      <h1>Click on a name for more info</h1>
    </div>
   <div class="">
   <table id="no-more-tables" class="table mon-table text-center table-light table-hover table-bordered table-margin" id="table">
   <div class="col-12 col-sm-5 col-lg-5 col-push-5">
   <thead class="thead-dark">
     <tr>
       <th>Name</th>
       <th>Image</th>
       <th>Family</th>
       <th>Element</th>
       <th>Description</th>
     </tr>
   </thead >
   <tbody id="table">
     <tr each='{monster in monsters}' role="button" data-href="/monsters/{monster.id}">
         <td data-title="Name">{monster.monsterName}</td>
         <td data-title="Image"><img src="{monster.image}" alt="{monster.name}" class="img-thumbnail"></td>
         <td data-title="Family">{monster.family}</td>
         <td data-title="Element">{monster.element}</td>
         <td data-title="Description">{monster.description}</td>
     </tr>
   </tbody>
   </div>
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
</monsters_list>