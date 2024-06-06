function skillsMember() {
  return {
    restrict: 'E',
    templateUrl: 'views/member/skills.html',
    controller: 'MemberSkillsController',
    controllerAs: 'vm',
    bindToController: true,
    scope: {
      member: '=',
      editable: '='
    }
  };
}