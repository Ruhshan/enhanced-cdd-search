export class SearchRequest {
    constructor(
        public seqinput = '',
        public selectedDatabase = 'cdd',
        public eValueThreshold = 0.1,
        public compositionBasedAdjustment = false,
        public rescueBorderLineHits = false,
        public suppressWeakOverLappingHits = false,
        public maxHit = 500
    ) {}
}

export class BatchSearchRequest {
    constructor(
        public queries = '',
        public selectedDatabase = 'cdd',
        public eValueThreshold = 0.01,
        public compositionCorrectedScoring = false,
        public applyLowComplexityFilter = false,
        public includeRetiredSequences = false,
        public maxHit = 500
    ) {}
}
