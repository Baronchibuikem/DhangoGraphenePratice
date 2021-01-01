describe("Navigation", function () {
  it("Can load homepage", function () {
    cy.visit("");
    cy.contains("Hi Welcome to RideConfy.").should("exist");
    cy.location().should((loc) => {
      expect(loc.host).to.eq("localhost:3006");
      //   expect(loc.pathname).to.eq("/sign-up");
    });
  });

  it("Can navigate to log in from sign up page", function () {
    cy.visit("/log-in");
    cy.get("a").contains("here").click();
    cy.location().should((loc) => {
      expect(loc.host).to.eq("localhost:3006");
      expect(loc.pathname).to.eq("/sign-up");
    });
  });

  it("Can navigate to login from sign up page", function () {
    cy.visit("/sign-up");
    cy.get("a").contains("here").click();
    cy.location().should((loc) => {
      expect(loc.host).to.eq("localhost:3006");
      expect(loc.pathname).to.eq("/log-in");
    });
  });
});
