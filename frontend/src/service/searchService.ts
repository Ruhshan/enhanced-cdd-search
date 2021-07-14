import { SearchRequest } from '@/types/searchRequest'
import { SearchResponse } from '@/types/searchResponse'

export default class SearchService {
    static async search(payload: SearchRequest): Promise<SearchResponse> {
        const data = {
            count: 5,
            data: [
                {
                    accession: 'pfam00230',
                    description:
                        'Major intrinsic protein; MIP (Major Intrinsic Protein) family proteins exhibit essentially two ...',
                    interval: '31-259',
                    evalue: '2.10e-88',
                    sequence:
                        'ELRSVSFLRAVIAEFLATLLFVFFGVGSALGVKKLVSSLAVSGLLAVALAFGLALATLVYCAGHISGAHLNPAVTLALLVGRRFSLLRAIFYIVAQLLGAIAGAALLYGVTVGLQRA-GLFANTLAPGVNAGQAFVVEIILTFQLVYCVFATTDdRRNGSLGTV---APLAIGFAVFLNHLAGGPYTGASMNPARSFGPAVVLWK---WDDHWVYWVGPFIGAALGALVY',
                },
                {
                    accession: 'cd00333',
                    description:
                        'Major intrinsic protein (MIP) superfamily. Members of the MIP superfamily function as membrane ...',
                    interval: '39-262',
                    evalue: '1.78e-76',
                    sequence:
                        'RKYLAEFLGTFLLVFFGCGSVLAVKLAGGA--SGGLLGIALAWGFAIFVLVYAVGHISGGHINPAVTLALAVGGRFPLIRVIPYIIAQLLGAILGAALLYGLYYGLYLEFLGANNivagifgtYPSPGVSNGNAFFVEFIGTFILVLVVFATTDDP--NGPPPGGLAPLAIGLLVAAIGLAGGPITGASMNPARSLGPALFTGLARHWHYFWVYWVGPLIGAIAGALVYDYV',
                },
                {
                    accession: 'TIGR00861',
                    description:
                        'MIP family channel proteins; 1.A.8 The Major Intrinsic Protein (MIP) FamilyThe MIP family is ...',
                    interval: '43-259',
                    evalue: '3.42e-66',
                    sequence:
                        'AEFLGTFLLVFFGVGSALGvnVAGAYGAVGGGQFLGVALAFGLAVATLVYCVGGISGAHLNPAVTIALLLGRRFPLKRVPVYIVAQLIGAILGAALLYGLTSGLFPGNLAVNGSASAGVSSGQAFFVEFIGTAILVLVIFATTDDRNRVPRG--GFAPLAIGLLVFLIHLSMGPYTGTGMNPARSLGPALFAGLAG-WGNHWVYWVGPIIGAILGALVY',
                },
                {
                    accession: 'COG0580',
                    description:
                        'Glycerol uptake facilitator and related aquaporins (Major Intrinsic Protein Family)  ...',
                    interval: '42-263',
                    evalue: '1.78e-44',
                    sequence:
                        'LAEFLGTFLLIFFGNGSVAAVALKGSKALGGGWLGIALAWGLGVLVAIYAFGGISGAHLNPAVTIALAVRGRFPWRKVLPYIVAQVLGAFAGAALLYLLYYGKILETEGDPLASLGafstspgGYSLGQAFLIEFVGTFVLVLGILALTDDGNANAG----FAPLAIGLLVTAIGLSLGPTTGTAINPARDLGPRLahslagwAANKGDSS-YFWIPVIGPIVGAILGALLYKLLL',
                },
                {
                    accession: 'PLN00027',
                    description: 'aquaporin TIP; Provisional',
                    interval: '39-256',
                    evalue: '5.77e-37',
                    sequence:
                        'KAALAEFISTLIFVFAGEGSGMAFNKLTDNGSTTpaGLVAAALAHAFALFVAVSVGANISGGHVNPAVTFGAFIGGNITLLRGILYWIAQLLGSVVACLLLKFSTGG----LETSAFSLSSGVGVWNAFVFEIVMTFGLVYTVYaTAVD---PKKGDLGIIAPIAIGFIVGANILAGGAFDGASMNPAVSFGPAVV---SWTWTNHWVYWAGPLIGGGIAG',
                },
            ],
        }
        const searchResponse = data as SearchResponse
        return Promise.resolve(searchResponse)
    }
}
