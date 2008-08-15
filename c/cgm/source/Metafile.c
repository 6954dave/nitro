/* =========================================================================
 * This file is part of NITRO
 * =========================================================================
 * 
 * (C) Copyright 2004 - 2008, General Dynamics - Advanced Information Systems
 *
 * NITRO is free software; you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public 
 * License along with this program;
 * If not, see <http://www.gnu.org/licenses/>.
 *
 */


#include "cgm/Metafile.h"


NITFAPI(cgm_Metafile*) cgm_Metafile_construct(nitf_Error* error)
{
    cgm_Metafile* mf = (cgm_Metafile*) NITF_MALLOC( sizeof(cgm_Metafile) );
    if (!mf)
    {
	nitf_Error_init(error, NITF_STRERROR(NITF_ERRNO), 
			NITF_CTXT, NITF_ERR_MEMORY);
	return NULL;
    }
    
    mf->name = NULL;
    mf->fontList = NULL;
    mf->description = NULL;
    mf->picture = NULL;
    
    return mf;
    
}
NITFAPI(void) cgm_Metafile_destruct(cgm_Metafile** mf)
{
    if (*mf)
    {
        
	if ( (*mf)->picture )
	{
	    cgm_Picture_destruct( & (*mf)->picture );
	}
        
	if ( (*mf)->fontList )
	{
	    /* We actually have to walk this to delete it */
	    
	    nitf_List_destruct(& (*mf)->fontList );
	}
        
	if ( (*mf)->name )
	{
	    NITF_FREE( (*mf)->name );
	}
        
	if ( (*mf)->description )
	{
	    NITF_FREE( (*mf)->description );
	}
        
	NITF_FREE( *mf );
	*mf = NULL;
    }
}
