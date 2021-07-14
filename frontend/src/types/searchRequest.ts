export class SearchRequest {
    constructor(
        public seqinput = '',
        public selectedDatabase = 'cdd',
        public eValueThreshold = 0.1,
        public compositionBasedAdjustment = false,
        public rescueBorderLineHits = false,
        public suppressWeakOverLappingHits = false,
        public maxHit = 500
    ) { }
}
