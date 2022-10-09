var WaterJugProblem = /** @class */ (function () {
    function WaterJugProblem(final, capacities) {
        this.final = final;
        this.capacities = capacities;
        this.init();
    }
    WaterJugProblem.prototype.init = function () {
        this.states = [[0, 0]];
    };
    WaterJugProblem.prototype.isStateExist = function (state) {
        return this.states.some(function (s) { return s[0] === state[0] && s[1] === state[1]; });
    };
    WaterJugProblem.prototype.checkFinalState = function (state) {
        return state[0] === this.final || state[1] === this.final;
    };
    return WaterJugProblem;
}());
